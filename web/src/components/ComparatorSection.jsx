import React, { useState } from 'react';
import { MODEL_METADATA, SAMPLES_METRICS } from '../data/samplesData';
import { Eye, Zap, ShieldCheck, CheckCircle2, XCircle, Maximize2, Target, Percent } from 'lucide-react';

function BoundingBoxIcon({ size = 15, color = "#64748B" }) {
  return (
    <svg viewBox="0 0 24 24" width={size} height={size} fill="none" stroke={color} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 8V4h4" />
      <path d="M20 8V4h-4" />
      <path d="M4 16v4h4" />
      <path d="M20 16v4h-4" />
      <rect x="7" y="7" width="10" height="10" rx="1.5" strokeDasharray="2 2" strokeWidth="1.5" />
    </svg>
  );
}

export function ComparatorSection({
  selectedSample,
  comparisonMode,
  modelLeft,
  modelRight
}) {
  const [activeModalImg, setActiveModalImg] = useState(null);

  const getImagePath = (sampleId, modelName) => {
    const base = import.meta.env.BASE_URL || "/";
    if (modelName === "Ground Truth") {
      return `${base}samples/${sampleId}/original.jpg`;
    }
    const meta = MODEL_METADATA[modelName];
    return `${base}samples/${sampleId}/${meta ? meta.filename : 'original.jpg'}`;
  };

  const getMetrics = (sampleId, modelName) => {
    if (modelName === "Ground Truth") return null;
    return SAMPLES_METRICS[sampleId]?.[modelName] || null;
  };

  const renderPanel = (panelTitle, modelName, isGT = false) => {
    const imgPath = getImagePath(selectedSample, isGT ? "Ground Truth" : modelName);
    const metrics = getMetrics(selectedSample, modelName);
    const meta = MODEL_METADATA[modelName] || {};

    // Métricas cuantitativas reales
    const getGtdCount = (sampleId) => {
      const counts = {
        "sample_01": 132,
        "sample_02": 83,
        "sample_03": 157,
        "sample_04": 206,
        "sample_05": 130
      };
      return counts[sampleId] || 54;
    };
    const gtCount = getGtdCount(selectedSample);

    const totalDetections = isGT ? gtCount : (metrics?.total_detections || 0);
    const tpCount = isGT ? gtCount : (metrics?.correct_detections || 0);
    const fpCount = isGT ? 0 : (metrics?.erroneous_detections || 0);
    const totalSum = tpCount + fpCount;
    const precisionPct = totalSum > 0 ? ((tpCount / totalSum) * 100).toFixed(1) : 0;
    const recallPct = gtCount > 0 ? ((tpCount / gtCount) * 100).toFixed(1) : 0;

    return (
      <div className="panel-card">
        {/* Envoltorio de la sección superior para garantizar alineación Y perfecta de las imágenes */}
        <div className="panel-upper-wrapper">
          {/* Cabecera y Metadatos discretos atenuados */}
          <div className="panel-header" style={{ flexDirection: 'column', alignItems: 'flex-start', gap: '2px', paddingBottom: '6px' }}>
            <h3 style={{ fontWeight: 800, fontSize: '1.05rem', color: '#0F172A', margin: 0 }}>
              {isGT ? "Ground Truth" : modelName}
            </h3>

            {/* Texto secundario discreto atenuado sin cajas de color */}
            {isGT ? (
              <p
                style={{
                  fontSize: '0.78rem',
                  color: '#64748B',
                  margin: 0,
                  fontWeight: 500,
                  minHeight: '40px',
                  display: 'flex',
                  alignItems: 'flex-start'
                }}
              >
                Imagen etiquetada manualmente
              </p>
            ) : meta.prompt ? (
              <p
                style={{
                  fontSize: '0.78rem',
                  color: '#64748B',
                  margin: 0,
                  fontWeight: 500,
                  width: '100%',
                  minWidth: 0,
                  minHeight: '40px',
                  display: 'flex',
                  alignItems: 'flex-start'
                }}
                title={`Prompt: "${meta.prompt}"`}
              >
                <span>
                  <strong style={{ color: '#C2410C', fontWeight: 600 }}>Prompt:</strong> "{meta.prompt}"
                </span>
              </p>
            ) : null}
          </div>

          {/* Tarjetas de Métricas Cuantitativas Principales (3 tarjetas por panel) */}
          <div className="metrics-kpi-grid">
            {isGT ? (
              <>
                {/* Anotaciones (GT) */}
                <div className="kpi-card">
                  <div className="kpi-header">
                    <span>Anotaciones</span>
                    <BoundingBoxIcon size={15} color="#64748B" />
                  </div>
                  <div className="kpi-value">{totalDetections}</div>
                </div>

                {/* Clases (GT) */}
                <div className="kpi-card">
                  <div className="kpi-header">
                    <span>Clases</span>
                    <Eye size={15} color="#64748B" />
                  </div>
                  <div className="kpi-value">2</div>
                </div>

                {/* Espaciador de reserva estructural para igualar las 3 tarjetas del modelo */}
                <div className="kpi-card" style={{ visibility: 'hidden' }} aria-hidden="true" />
              </>
            ) : (
              <>
                {/* Total Detecciones */}
                <div className="kpi-card">
                  <div className="kpi-header">
                    <span>Total Detecciones</span>
                    <BoundingBoxIcon size={15} color="#64748B" />
                  </div>
                  <div className="kpi-value">{totalDetections}</div>
                </div>

                {/* Correctas (TP) */}
                <div className="kpi-card tp-card">
                  <div className="kpi-header">
                    <span>Correctas (TP)</span>
                    <CheckCircle2 size={14} color="#166534" />
                  </div>
                  <div className="kpi-value">{tpCount}</div>
                </div>

                {/* Errores (FP) */}
                <div className="kpi-card fp-card">
                  <div className="kpi-header">
                    <span>Errores (FP)</span>
                    <XCircle size={14} color="#991B1B" />
                  </div>
                  <div className="kpi-value">{fpCount}</div>
                </div>
              </>
            )}
          </div>
        </div>

        {/* Visor de Imagen con Etiquetado Visual y Overlay de FPS */}
        <div className="image-box">
          <img src={imgPath} alt={panelTitle} loading="lazy" />

          {/* Unified Model Metrics Overlay Badge (Esquina superior derecha) */}
          {!isGT && (
            <div
              style={{
                position: 'absolute',
                top: '10px',
                right: '10px',
                background: 'rgba(15, 23, 42, 0.78)',
                backdropFilter: 'blur(8px)',
                WebkitBackdropFilter: 'blur(8px)',
                color: '#94A3B8',
                border: '1px solid rgba(255, 255, 255, 0.18)',
                borderRadius: '6px',
                padding: '4px 10px',
                fontSize: '0.74rem',
                fontWeight: 600,
                boxShadow: '0 4px 12px rgba(0, 0, 0, 0.3)',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                zIndex: 10,
                whiteSpace: 'nowrap'
              }}
            >
              {meta.fps && (
                <>
                  <span title="Imágenes procesadas por segundo (Inferencia)">
                    FPS: <span style={{ color: '#F8FAFC', fontWeight: 700 }}>{meta.fps}</span>
                  </span>
                  <span style={{ color: 'rgba(255, 255, 255, 0.2)', fontWeight: 300 }}>|</span>
                </>
              )}
              <span title="Precisión (Exactitud de las detecciones)">
                Prec: <span style={{ color: '#F8FAFC', fontWeight: 700 }}>{precisionPct}%</span>
              </span>
              <span style={{ color: 'rgba(255, 255, 255, 0.2)', fontWeight: 300 }}>|</span>
              <span title="Recall (Porcentaje de objetos reales detectados)">
                Rec: <span style={{ color: '#F8FAFC', fontWeight: 700 }}>{recallPct}%</span>
              </span>
            </div>
          )}

          {/* Botón Ampliar (Esquina inferior derecha) */}
          <button
            onClick={() => setActiveModalImg({ title: panelTitle, imgPath })}
            style={{
              position: 'absolute',
              bottom: '10px',
              right: '10px',
              background: 'rgba(15, 23, 42, 0.75)',
              backdropFilter: 'blur(8px)',
              WebkitBackdropFilter: 'blur(8px)',
              color: '#F8FAFC',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              borderRadius: '6px',
              padding: '5px 10px',
              fontSize: '0.75rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '5px',
              boxShadow: '0 4px 12px rgba(0, 0, 0, 0.25)',
              zIndex: 10
            }}
          >
            <Maximize2 size={13} /> Ampliar
          </button>
        </div>



        {/* Desglose por Clase como Lista Compacta Ordenada (Solo para modelos, no en Ground Truth) */}
        {!isGT && metrics?.by_class && (
          <div className="class-breakdown-box">
            <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#64748B', marginBottom: '2px' }}>
              Desglose por Clase de Fruto:
            </div>

            <div className="class-breakdown-table-wrapper">
              <table className="class-breakdown-table">
                <thead>
                  <tr>
                    <th>Clase</th>
                    <th>Total</th>
                    <th>Correctas (TP)</th>
                    <th>Errores (FP)</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(metrics.by_class).map(([cls, stats]) => {
                    const isRipe = cls === 'Naranja';
                    return (
                      <tr key={cls}>
                        <td style={{ fontWeight: 700 }}>
                          <span className={`bbox-swatch ${isRipe ? 'bbox-swatch-red' : 'bbox-swatch-blue'}`} style={{ marginRight: '8px' }} />
                          {isRipe ? 'Naranja Madura' : 'Naranja Verde'}
                        </td>
                        <td>{stats.total}</td>
                        <td style={{ color: '#059669', fontWeight: 700 }}>{stats.correct}</td>
                        <td style={{ color: '#DC2626', fontWeight: 700 }}>{stats.erroneous}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <section className="card-section">
      <div className="section-title">
        <Eye color="#F97316" size={24} />
        <span>Comparador Visual e Inferencia de Modelos</span>
      </div>
      <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginBottom: '16px' }}>
        {comparisonMode === 'gt_vs_model'
          ? "Visualiza la precisión de las detecciones realizadas por cada modelo comparadas con el etiquetado manual (Ground Truth)."
          : "Compara de forma directa las detecciones y el rendimiento entre dos modelos de Inteligencia Artificial."}
      </p>

      {/* Leyenda de Bounding Boxes */}
      <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap', background: '#FFFFFF', padding: '10px 18px', borderRadius: '8px', border: '1px solid #E2E8F0', marginBottom: '16px', fontSize: '0.82rem', fontWeight: 600, boxShadow: '0 1px 3px rgba(0,0,0,0.02)' }}>
        <span style={{ color: '#64748B', fontWeight: 700 }}>Leyenda:</span>
        <span style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#0F172A' }}><span className="bbox-swatch bbox-swatch-red" /> Naranja Madura</span>
        <span style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#0F172A' }}><span className="bbox-swatch bbox-swatch-blue" /> Naranja Verde</span>
        <span style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#0F172A' }}><span className="bbox-swatch bbox-swatch-gt" /> Ground Truth</span>
      </div>

      <div className="comparator-grid">
        {comparisonMode === "gt_vs_model" ? (
          <>
            {renderPanel("Ground Truth", "Ground Truth", true)}
            {renderPanel(modelLeft, modelLeft, false)}
          </>
        ) : (
          <>
            {renderPanel(modelLeft, modelLeft, false)}
            {renderPanel(modelRight, modelRight, false)}
          </>
        )}
      </div>

      {/* Modal Ampliación */}
      {activeModalImg && (
        <div
          onClick={() => setActiveModalImg(null)}
          style={{
            position: 'fixed',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.85)',
            zIndex: 2000,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px'
          }}
        >
          <div style={{ maxWidth: '90vw', maxHeight: '90vh', textCenter: 'center' }}>
            <img src={activeModalImg.imgPath} alt={activeModalImg.title} style={{ maxWidth: '100%', maxHeight: '85vh', borderRadius: '10px' }} />
            <div style={{ color: '#FFF', textAlign: 'center', marginTop: '10px', fontWeight: 700 }}>
              {activeModalImg.title} (Haz clic en cualquier punto para cerrar)
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
