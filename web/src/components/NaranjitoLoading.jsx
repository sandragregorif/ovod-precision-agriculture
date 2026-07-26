import React, { useState, useEffect } from 'react';
import { NaranjitoIcon } from './NaranjitoChatbotDrawer';

const LOADING_MESSAGES = [
  "Buscando en la investigación...",
  "Analizando los datos del TFG...",
  "Consultando los resultados...",
  "Revisando los modelos evaluados...",
  "Preparando la respuesta...",
];

const NaranjitoLoading = () => {
  const [messageIndex, setMessageIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setMessageIndex((prev) => (prev + 1) % LOADING_MESSAGES.length);
    }, 2200);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="naranjito-loading">
      <div className="naranjito-loading-icon">
        <NaranjitoIcon size={36} />
      </div>
      <div className="naranjito-loading-text">
        {LOADING_MESSAGES[messageIndex]}
      </div>
    </div>
  );
};

export default NaranjitoLoading;
