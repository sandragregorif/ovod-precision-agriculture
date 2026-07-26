import React, { useState, useRef, useEffect } from 'react';
import { X, Send, Sparkles, RefreshCw, MessageSquare } from 'lucide-react';
import NaranjitoLoading from './NaranjitoLoading';

const INITIAL_SUGGESTIONS = [
  "¿De qué trata esta investigación?",
  "¿Cuáles fueron las conclusiones finales de la investigación?",
  "¿Qué modelos de detección de objetos de vocabulario abierto (OVOD) se utilizaron en el proyecto?",
  "¿Qué aplicaciones tiene esto en la agricultura real?"
];

const stripSuggestionsPrefix = (text) => {
  if (!text) return '';
  if (text.toLowerCase().includes('[')) {
    const lastBracketIdx = text.lastIndexOf('[');
    const afterBracket = text.substring(lastBracketIdx).toLowerCase();
    if ("[sugerencias]".startsWith(afterBracket)) {
      return text.substring(0, lastBracketIdx).trim();
    }
  }
  const target = "SUGERENCIAS";
  for (let len = target.length; len >= 3; len--) {
    const prefix = target.substring(0, len);
    if (text.toLowerCase().endsWith(prefix.toLowerCase())) {
      return text.substring(0, text.length - len).trim();
    }
  }
  return text;
};

const renderMarkdown = (text) => {
  if (!text) return '';
  const lines = text.split('\n');
  return lines.map((line, lineIdx) => {
    const isBullet = line.trim().startsWith('- ') || line.trim().startsWith('* ');
    const isNumList = /^\d+\.\s/.test(line.trim());
    
    let content = line;
    if (isBullet) {
      content = line.trim().substring(2);
    } else if (isNumList) {
      content = line.trim().substring(line.trim().indexOf(' ') + 1);
    }
    
    const parseInline = (str) => {
      const boldParts = str.split('**');
      return boldParts.flatMap((boldPart, boldIndex) => {
        const isBold = boldIndex % 2 === 1;
        const italicParts = boldPart.split('*');
        const renderedItalics = italicParts.map((italicPart, italicIndex) => {
          const isItalic = italicIndex % 2 === 1;
          if (isItalic) {
            return <em key={`${boldIndex}-${italicIndex}`}>{italicPart}</em>;
          }
          return italicPart;
        });
        
        if (isBold) {
          return <strong key={boldIndex}>{renderedItalics}</strong>;
        }
        return renderedItalics;
      });
    };

    const renderedContent = parseInline(content);

    if (isBullet) {
      return (
        <li key={lineIdx} style={{ marginLeft: '8px', listStyleType: 'disc', listStylePosition: 'inside', margin: '4px 0' }}>
          {renderedContent}
        </li>
      );
    }
    if (isNumList) {
      return (
        <li key={lineIdx} style={{ marginLeft: '8px', listStyleType: 'decimal', listStylePosition: 'inside', margin: '4px 0' }}>
          {renderedContent}
        </li>
      );
    }
    
    return (
      <p key={lineIdx} style={{ margin: '0 0 6px 0', minHeight: '1em' }}>
        {renderedContent}
      </p>
    );
  });
};

export function NaranjitoIcon({ size = 36 }) {
  return (
    <svg viewBox="0 0 100 100" style={{ width: `${size}px`, height: `${size}px`, flexShrink: 0 }}>
      <defs>
        <linearGradient id="naranjitoSvgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#FB923C" />
          <stop offset="50%" stopColor="#F97316" />
          <stop offset="100%" stopColor="#EA580C" />
        </linearGradient>
      </defs>
      <circle cx="50" cy="52" r="46" fill="url(#naranjitoSvgGrad)" stroke="#FFFFFF" strokeWidth="3" />
      <circle cx="35" cy="28" r="10" fill="#FFFFFF" opacity="0.25" />
      <path d="M50 8 C50 -4, 70 0, 68 12 Z" fill="#10B981" />
      <path d="M50 8 L50 16" stroke="#059669" strokeWidth="4" strokeLinecap="round" />
      <circle cx="50" cy="4" r="4" fill="#FBBF24" />
      <rect x="30" y="42" width="11" height="14" rx="5.5" fill="#0F172A" />
      <rect x="59" y="42" width="11" height="14" rx="5.5" fill="#0F172A" />
      <circle cx="33" cy="45" r="2.8" fill="#FFFFFF" />
      <circle cx="62" cy="45" r="2.8" fill="#FFFFFF" />
      <ellipse cx="23" cy="58" rx="6" ry="3.5" fill="#F43F5E" opacity="0.5" />
      <ellipse cx="77" cy="58" rx="6" ry="3.5" fill="#F43F5E" opacity="0.5" />
      <path d="M38 60 Q50 73 62 60" stroke="#0F172A" strokeWidth="4" strokeLinecap="round" fill="none" />
    </svg>
  );
}

export function FarmerIcon({ size = 36 }) {
  return (
    <svg viewBox="0 0 100 100" style={{ width: `${size}px`, height: `${size}px`, flexShrink: 0 }}>
      <defs>
        <linearGradient id="farmerSvgGradInside" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#38BDF8" />
          <stop offset="100%" stopColor="#22C55E" />
        </linearGradient>
      </defs>
      {/* Círculo de fondo con cielo azul y campo verde */}
      <circle cx="50" cy="50" r="46" fill="url(#farmerSvgGradInside)" stroke="#FFFFFF" strokeWidth="3" />
      
      {/* Cuerpo del agricultor (Camisa y peto) */}
      <path d="M22 88 C22 72, 32 66, 50 66 C68 66, 78 72, 78 88 Z" fill="#1E3A8A" />
      <path d="M38 66 L50 78 L62 66 Z" fill="#F87171" />
      
      {/* Tirantes del peto */}
      <rect x="30" y="68" width="8" height="20" fill="#FBBF24" rx="2" />
      <rect x="62" y="68" width="8" height="20" fill="#FBBF24" rx="2" />
      <circle cx="34" cy="74" r="2.5" fill="#B45309" />
      <circle cx="66" cy="74" r="2.5" fill="#B45309" />

      {/* Cabeza */}
      <circle cx="50" cy="50" r="18" fill="#FDBA74" />
      
      {/* Sombrero de paja */}
      {/* Copa del sombrero */}
      <path d="M32 36 C32 20, 68 20, 68 36 Z" fill="#EAB308" stroke="#CA8A04" strokeWidth="1.5" />
      {/* Cinta del sombrero */}
      <path d="M32 35 C38 32, 62 32, 68 35 L68 38 C62 35, 38 35, 32 38 Z" fill="#E11D48" />
      {/* Ala del sombrero */}
      <ellipse cx="50" cy="38" rx="28" ry="7" fill="#FACC15" stroke="#EAB308" strokeWidth="1.5" />
      
      {/* Detalles de la cara */}
      <circle cx="43" cy="48" r="2" fill="#1E293B" />
      <circle cx="57" cy="48" r="2" fill="#1E293B" />
      <circle cx="37" cy="52" r="3" fill="#F43F5E" opacity="0.4" />
      <circle cx="63" cy="52" r="3" fill="#F43F5E" opacity="0.4" />
      <path d="M44 54 Q50 60 56 54" stroke="#1E293B" strokeWidth="2.5" strokeLinecap="round" fill="none" />
    </svg>
  );
}

export function NaranjitoChatbotDrawer() {
  const [isOpen, setIsOpen] = useState(false);
  const [showCallout, setShowCallout] = useState(true);
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: '¡Hola! Soy **Naranjito**. Hazme cualquier consulta sobre el TFG de **Sandra Gregori Fernández** (metodología, resultados, prompts) o sobre el funcionamiento de la demo.',
      suggestions: INITIAL_SUGGESTIONS
    }
  ]);
  const [inputQuery, setInputQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (isOpen) {
      chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, isOpen, loading]);

  const handleSend = async (queryText) => {
    const textToSend = queryText || inputQuery.trim();
    if (!textToSend || loading) return;

    setMessages((prev) => [...prev, { role: 'user', content: textToSend }]);
    setInputQuery('');
    setLoading(true);

    const historyQuestions = messages.filter(m => m.role === 'user').map(m => m.content);
    historyQuestions.push(textToSend);

    try {
      let rawApiUrl = import.meta.env.VITE_API_URL || `http://${window.location.hostname}:8000`;
      let baseUrl = rawApiUrl.replace(/\/+$|\/(ask|chat)(\/stream)?$/g, '');
      const streamUrl = `${baseUrl}/chat/stream`;

      const res = await fetch(streamUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: textToSend,
          chat_history: historyQuestions
        })
      });

      if (res.ok && res.body) {
        let assistantMessage = { role: 'assistant', content: '', suggestions: [] };
        let hasStartedStreaming = false;
        let targetText = '';
        let currentText = '';
        let animTimer = null;

        const updateTypewriter = () => {
          if (currentText.length < targetText.length) {
            const diff = targetText.length - currentText.length;
            const step = diff > 40 ? 5 : diff > 15 ? 3 : diff > 5 ? 2 : 1;
            currentText = targetText.substring(0, currentText.length + step);
            assistantMessage.content = stripSuggestionsPrefix(currentText);
            setMessages((prev) => {
              const updated = [...prev];
              updated[updated.length - 1] = { ...assistantMessage };
              return updated;
            });
          }
        };

        animTimer = setInterval(updateTypewriter, 16);

        const reader = res.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let buffer = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split('\n\n');
          buffer = lines.pop() || '';

          for (const line of lines) {
            const trimmed = line.trim();
            if (!trimmed.startsWith('data:')) continue;
            const dataStr = trimmed.substring(5).trim();
            if (dataStr === '[DONE]') continue;

            try {
              const data = JSON.parse(dataStr);
              if (data.type === 'token') {
                if (!hasStartedStreaming) {
                  hasStartedStreaming = true;
                  setLoading(false);
                  setMessages((prev) => [...prev, assistantMessage]);
                }
                targetText += data.content;
              } else if (data.type === 'suggestions') {
                if (!hasStartedStreaming) {
                  hasStartedStreaming = true;
                  setLoading(false);
                  setMessages((prev) => [...prev, assistantMessage]);
                }
                if (data.full_answer) {
                  targetText = data.full_answer;
                }
                assistantMessage.suggestions = data.items || [];
              }
            } catch (parseErr) {
              console.error("Error parsing SSE data:", parseErr);
            }
          }
        }

        while (currentText.length < targetText.length) {
          await new Promise((resolve) => setTimeout(resolve, 20));
        }
        clearInterval(animTimer);
        assistantMessage.content = stripSuggestionsPrefix(targetText);
        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1] = { ...assistantMessage };
          return updated;
        });
      } else {
        throw new Error();
      }
    } catch (e) {
      let reply = "";
      const queryLower = textToSend.toLowerCase();

      if (queryLower.includes("conclusión") || queryLower.includes("conclusiones")) {
        reply = "Las conclusiones principales del TFG muestran que **OWLv2** obtuvo el F1-score general más alto (**0.519**). Para entornos de tiempo real, **YOLO-World** (0.456 F1) y **YOLOE** (0.447 F1) ofrecen el mejor compromiso con velocidades de 8-9 FPS. Las naranjas verdes siguen siendo el mayor reto por camuflaje.";
      } else if (queryLower.includes("evaluaron") || queryLower.includes("qué modelos") || queryLower.includes("lista de modelos")) {
        reply = "Los 5 modelos de vocabulario abierto (OVOD) evaluados en este Trabajo de Fin de Grado son: **YOLO-World**, **YOLOE**, **OWLv2**, **Grounding DINO** y **SAM 3**.";
      } else if (queryLower.includes("rápido") || queryLower.includes("velocidad") || queryLower.includes("modelo") || queryLower.includes("destacó") || queryLower.includes("destacaron")) {
        reply = "**YOLOE** y **YOLO-World** demostraron la mayor velocidad de procesamiento (8.99 FPS y 8.10 FPS respectivamente), con un F1-score de 0.447 y 0.456. **OWLv2** es el más preciso con 0.519 F1 pero inviable en tiempo real (0.34 FPS).";
      } else if (queryLower.includes("verde") || queryLower.includes("dificultad") || queryLower.includes("reto")) {
        reply = "Las naranjas verdes presentan un F1-score sustancialmente menor debido al **camuflaje cromático** con las hojas del naranjo y a los reflejos especulares de la luz solar en las hojas y frutos.";
      } else if (queryLower.includes("tiling") || queryLower.includes("parche") || queryLower.includes("parches") || queryLower.includes("ventajas")) {
        reply = "La técnica de **Tiling** (procesamiento por parches solapados) solucionó la pérdida de resolución en imágenes de gran tamaño, mejorando la detección de frutos pequeños y lejanos a costa de un incremento en el tiempo de cómputo.";
      } else if (queryLower.includes("map") || queryLower.includes("resultado") || queryLower.includes("resultados") || queryLower.includes("f1")) {
        reply = "Los resultados de F1-score en el conjunto de test global son: **OWLv2** (0.519), **YOLO-World** (0.456), **YOLOE** (0.447), **Grounding DINO** (0.311) y **SAM 3** (0.150).";
      } else if (queryLower.includes("demo") || queryLower.includes("arquitectura") || queryLower.includes("funciona") || queryLower.includes("funcionamiento")) {
        reply = "La demo interactiva se organiza de la siguiente manera:\n\n- **El Comparador Visual de Modelos (la pantalla principal)**: Permite comparar modelos entre sí o contrastar de forma interactiva las detecciones de naranjas (maduras y verdes) realizadas por las 5 arquitecturas evaluadas (YOLO-World, YOLOE, OWLv2, Grounding DINO y SAM 3) frente al etiquetado real (Ground Truth).\n\n- **El Asistente Naranjito**: Un chatbot conversacional concebido para resolver dudas académicas de la memoria del TFG y detallar los resultados semánticos del proyecto. También permite consultar la guia de la demo.";
      } else if (queryLower.includes("aplicación") || queryLower.includes("aplicacion") || queryLower.includes("aplicaciones") || queryLower.includes("agricultura real") || queryLower.includes("campo")) {
        reply = "Las aplicaciones prácticas en agricultura real de este desarrollo incluyen:\n\n1. **Estimación automatizada de rendimiento de cosecha**: Estimación dinámica mediante el conteo del volumen y madurez de frutos a gran escala.\n2. **Guiado autónomo y robótica**: Integración de visión computacional en vehículos recolectores y tractores inteligentes.\n3. **Monitoreo inteligente**: Operatividad local y bajo coste gracias a modelos eficientes (como YOLOE y YOLO-World) ejecutables en dispositivos de borde.\n\nPara maximizar el éxito en producción, se recomienda desacoplar la inferencia en modelos específicos por tipo de cultivo.";
      } else {
        reply = "Esta investigación evalúa y compara modelos de visión por computador de vocabulario abierto (OVOD) para la detección y conteo de naranjas maduras y verdes en el ámbito de la agricultura de precisión.";
      }

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: reply,
          suggestions: [
            "¿Cuáles fueron los resultados de F1-score?",
            "¿Qué ventajas aporta el Tiling?",
            "¿Qué modelos se evaluaron?"
          ]
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleToggleOpen = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      setShowCallout(false);
    }
  };

  return (
    <>
      {/* Bocadillo/Callout informativo flotante */}
      {showCallout && !isOpen && (
        <div className="naranjito-callout-bubble" onClick={handleToggleOpen}>
          <span>¿Tienes dudas? ¡Pregúntame!</span>
          <button
            className="naranjito-callout-close"
            onClick={(e) => {
              e.stopPropagation();
              setShowCallout(false);
            }}
          >
            <X size={14} />
          </button>
          <div className="naranjito-callout-arrow" />
        </div>
      )}

      {/* Botón flotante Naranjito */}
      <button
        className="naranjito-float-btn"
        onClick={handleToggleOpen}
        title="Consultar al Asistente Naranjito (RAG)"
      >
        <NaranjitoIcon size={66} />
      </button>

      {/* Drawer lateral derecho colapsable */}
      <div className={`naranjito-drawer-panel ${isOpen ? 'open' : ''}`}>
        <div className="drawer-header">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <NaranjitoIcon size={38} />
            <div>
              <h3 style={{ fontSize: '1rem', fontWeight: 800, color: '#7C2D12' }}>Asistente Naranjito</h3>
              <p style={{ fontSize: '0.74rem', color: '#C2410C', fontWeight: 600 }}>RAG sobre el TFG y la demo</p>
            </div>
          </div>
          <button className="drawer-close-btn" onClick={() => setIsOpen(false)}>
            <X size={20} />
          </button>
        </div>

        <div className="drawer-messages">
          {messages.map((m, idx) => (
            <div key={idx} className={`drawer-chat-bubble ${m.role}`}>
              {m.role === 'assistant' ? (
                <NaranjitoIcon size={32} />
              ) : (
                <FarmerIcon size={32} />
              )}
              <div className="drawer-chat-text">
                <div>{renderMarkdown(m.content)}</div>

                {m.role === 'assistant' && m.suggestions && m.suggestions.length > 0 && (
                  <div style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <div style={{ fontSize: '0.72rem', fontWeight: 700, color: '#C2410C' }}>Preguntas sugeridas:</div>
                    {m.suggestions.map((sug, sIdx) => (
                      <button
                        key={sIdx}
                        onClick={() => handleSend(sug)}
                        style={{
                          background: '#FFF7ED',
                          border: '1px solid #FDBA74',
                          color: '#9A3412',
                          padding: '6px 10px',
                          borderRadius: '8px',
                          fontSize: '0.78rem',
                          fontWeight: 600,
                          textAlign: 'left',
                          cursor: 'pointer'
                        }}
                      >
                        {sug}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="drawer-chat-bubble assistant">
              <NaranjitoLoading />
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="drawer-input-area">
          <input
            type="text"
            className="drawer-input"
            placeholder="Pregunta a Naranjito..."
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            disabled={loading}
          />
          <button className="drawer-send-btn" onClick={() => handleSend()} disabled={loading || !inputQuery.trim()}>
            <Send size={16} />
          </button>
        </div>
      </div>
    </>
  );
}
