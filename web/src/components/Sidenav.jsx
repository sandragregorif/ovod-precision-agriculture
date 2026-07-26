import React from 'react';
import { ALL_MODELS, SAMPLES_LIST } from '../data/samplesData';
import { Sliders, Eye, Settings2, X } from 'lucide-react';

export function Sidenav({
  selectedSample,
  setSelectedSample,
  comparisonMode,
  setComparisonMode,
  modelLeft,
  setModelLeft,
  modelRight,
  setModelRight,
  isOpen,
  onClose
}) {
  return (
    <aside className={`sidenav-container ${isOpen ? 'open' : ''}`}>
      <div className="sidenav-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
        <div>
          <h1 className="sidenav-title">Demo OVOD</h1>
          <div className="sidenav-subtitle">Sandra Gregori • Agricultura de Precisión</div>
        </div>
        <button
          className="sidenav-close-btn"
          onClick={onClose}
          title="Cerrar Ajustes"
          aria-label="Cerrar Ajustes"
        >
          <X size={20} />
        </button>
      </div>

      {/* Sección 1: Selección de Muestra */}
      <div className="sidenav-section">
        <div className="sidenav-section-title">
          <Eye size={14} style={{ display: 'inline', marginRight: '6px' }} />
          Imagen de Evaluación
        </div>
        <div className="form-group">
          <label className="form-label">Seleccionar Imagen:</label>
          <select
            className="form-select"
            value={selectedSample}
            onChange={(e) => setSelectedSample(e.target.value)}
          >
            {SAMPLES_LIST.map((s) => (
              <option key={s.id} value={s.id}>
                {s.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Sección 2: Modo de Comparación */}
      <div className="sidenav-section">
        <div className="sidenav-section-title">
          <Sliders size={14} style={{ display: 'inline', marginRight: '6px' }} />
          Tipo de Comparativa
        </div>
        <div className="radio-segmented">
          <button
            className={`radio-segmented-btn ${comparisonMode === 'gt_vs_model' ? 'active' : ''}`}
            onClick={() => setComparisonMode('gt_vs_model')}
          >
            GT vs Modelo
          </button>
          <button
            className={`radio-segmented-btn ${comparisonMode === 'model_vs_model' ? 'active' : ''}`}
            onClick={() => {
              setComparisonMode('model_vs_model');
              if (modelLeft === modelRight) {
                const fallback = ALL_MODELS.find((m) => m !== modelLeft);
                if (fallback) setModelRight(fallback);
              }
            }}
          >
            Modelo vs Modelo
          </button>
        </div>
      </div>

      {/* Sección 3: Selección de Modelos */}
      <div className="sidenav-section">
        <div className="sidenav-section-title">
          <Settings2 size={14} style={{ display: 'inline', marginRight: '6px' }} />
          Modelos OVOD
        </div>

        {comparisonMode === 'gt_vs_model' ? (
          <div className="form-group">
            <label className="form-label">Modelo a Evaluar:</label>
            <select
              className="form-select"
              value={modelLeft}
              onChange={(e) => {
                const newVal = e.target.value;
                setModelLeft(newVal);
                if (newVal === modelRight) {
                  const fallback = ALL_MODELS.find((m) => m !== newVal);
                  if (fallback) setModelRight(fallback);
                }
              }}
            >
              {ALL_MODELS.map((m) => (
                <option key={m} value={m}>
                  {m}
                </option>
              ))}
            </select>
          </div>
        ) : (
          <>
            <div className="form-group">
              <label className="form-label">Modelo Izquierda (A):</label>
              <select
                className="form-select"
                value={modelLeft}
                onChange={(e) => {
                  const newVal = e.target.value;
                  setModelLeft(newVal);
                  if (newVal === modelRight) {
                    const fallback = ALL_MODELS.find((m) => m !== newVal);
                    if (fallback) setModelRight(fallback);
                  }
                }}
              >
                {ALL_MODELS.map((m) => (
                  <option key={m} value={m}>
                    {m}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label className="form-label">Modelo Derecha (B):</label>
              <select
                className="form-select"
                value={modelRight}
                onChange={(e) => setModelRight(e.target.value)}
              >
                {ALL_MODELS.filter((m) => m !== modelLeft).map((m) => (
                  <option key={m} value={m}>
                    {m}
                  </option>
                ))}
              </select>
            </div>
          </>
        )}
      </div>

      {/* Nota pie de sidenav */}
      <div style={{ marginTop: 'auto', paddingTop: '16px', borderTop: '1px solid var(--border-light)', fontSize: '0.76rem', color: 'var(--text-muted)' }}>
        <div>Trabajo de Fin de Grado en Ingeniería Informática (UPV 2026)</div>
        <div style={{ fontWeight: 600, color: 'var(--text-title)', marginTop: '2px' }}>Autora: Sandra Gregori Fernández</div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginTop: '10px' }}>
          <a
            href="https://github.com/sandragregorif?tab=repositories"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '5px',
              color: '#334155',
              textDecoration: 'none',
              fontSize: '0.78rem',
              fontWeight: 600,
              transition: 'color 0.2s'
            }}
            title="Repositorio GitHub"
          >
            <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
            </svg>
            <span>GitHub</span>
          </a>
          <span style={{ opacity: 0.35 }}>•</span>
          <a
            href="https://linkedin.com/in/sandragregorif"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '5px',
              color: '#0A66C2',
              textDecoration: 'none',
              fontSize: '0.78rem',
              fontWeight: 600,
              transition: 'color 0.2s'
            }}
            title="Perfil LinkedIn"
          >
            <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
              <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.4 1.4 0 1 0 0 2.8 1.4 1.4 0 0 0 0-2.8z" />
            </svg>
            <span>LinkedIn</span>
          </a>
        </div>
      </div>
    </aside>
  );
}
