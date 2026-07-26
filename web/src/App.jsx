import React, { useState, useEffect } from 'react';
import { Sidenav } from './components/Sidenav';
import { ComparatorSection } from './components/ComparatorSection';
import { RankingTableSection } from './components/RankingTableSection';
import { NaranjitoChatbotDrawer } from './components/NaranjitoChatbotDrawer';
import { FileText, ExternalLink, Sliders } from 'lucide-react';

export function App() {
  const [selectedSample, setSelectedSample] = useState("sample_01");
  const [comparisonMode, setComparisonMode] = useState("gt_vs_model");
  const [modelLeft, setModelLeft] = useState("YOLO-World");
  const [modelRight, setModelRight] = useState("Grounding DINO");
  const [isMobileSidenavOpen, setIsMobileSidenavOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="landing-layout">
      {/* Barra superior de control visible sólo en móviles */}
      <header className="mobile-navbar">
        <div className="mobile-navbar-brand">
          <div className="mobile-navbar-dot" />
          <h1 className="mobile-navbar-title">Demo OVOD</h1>
        </div>
        <button
          className={`mobile-navbar-toggle-btn ${isScrolled ? 'floating' : ''}`}
          onClick={() => setIsMobileSidenavOpen(true)}
          title="Ver Ajustes"
        >
          <Sliders size={18} />
          <span>Ajustes</span>
        </button>
      </header>

      {/* Backdrop para cerrar el Sidenav en móviles */}
      {isMobileSidenavOpen && (
        <div
          className="sidenav-backdrop"
          onClick={() => setIsMobileSidenavOpen(false)}
        />
      )}

      {/* Sidenav de ajustes (Izquierda) */}
      <Sidenav
        selectedSample={selectedSample}
        setSelectedSample={setSelectedSample}
        comparisonMode={comparisonMode}
        setComparisonMode={setComparisonMode}
        modelLeft={modelLeft}
        setModelLeft={setModelLeft}
        modelRight={modelRight}
        setModelRight={setModelRight}
        isOpen={isMobileSidenavOpen}
        onClose={() => setIsMobileSidenavOpen(false)}
      />

      {/* Área Central Principal */}
      <main className="main-landing-content">
        {/* Banner Superior */}
        <div className="hero-banner">
          <div>
            <h1 className="hero-title">
              Detección de Objetos de Vocabulario Abierto (OVOD)
            </h1>
            <p className="hero-description">
              Evaluación y comparativa cuantitativa de modelos de detección de objetos de vocabulario abierto en el dominio de la agricultura de precisión (detección de naranjas maduras e inmaduras)
            </p>
            <div style={{ marginTop: '14px' }}>
              <a
                href="https://drive.google.com/file/d/1J17j2dLcabe-jr5-lRW-YQ6UqXoOMr-0/view?usp=sharing"
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  color: '#C2410C',
                  textDecoration: 'none',
                  background: '#FFF7ED',
                  border: '1px solid #FFEDD5',
                  padding: '6px 14px',
                  borderRadius: '20px',
                  boxShadow: '0 1px 2px rgba(0,0,0,0.03)',
                  transition: 'all 0.2s ease'
                }}
              >
                <FileText size={15} color="#EA580C" />
                <span>Ver memoria del TFG</span>
                <ExternalLink size={13} style={{ opacity: 0.6 }} />
              </a>
            </div>
          </div>
        </div>

        {/* 1. Comparador Visual */}
        <ComparatorSection
          selectedSample={selectedSample}
          comparisonMode={comparisonMode}
          modelLeft={modelLeft}
          modelRight={modelRight}
        />

        {/* 2. Tabla de Rendimiento Global en Test */}
        <RankingTableSection />
      </main>

      {/* Botón flotante Naranjito + Drawer lateral derecho colapsable */}
      <NaranjitoChatbotDrawer />
    </div>
  );
}

export default App;
