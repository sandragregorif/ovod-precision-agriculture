import React, { useState } from 'react';
import { GLOBAL_RANKING } from '../data/samplesData';
import { Table, ArrowUpDown, ArrowUp, ArrowDown } from 'lucide-react';

export function RankingTableSection() {
  const [sortColumn, setSortColumn] = useState('f1');
  const [sortDirection, setSortDirection] = useState('desc');

  const handleSort = (columnKey) => {
    if (sortColumn === columnKey) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(columnKey);
      setSortDirection('desc');
    }
  };

  const sortedData = [...GLOBAL_RANKING].sort((a, b) => {
    let valA = a[sortColumn];
    let valB = b[sortColumn];

    if (sortColumn === 'model') {
      return sortDirection === 'asc'
        ? valA.localeCompare(valB)
        : valB.localeCompare(valA);
    }

    const numA = parseFloat(valA) || 0;
    const numB = parseFloat(valB) || 0;

    return sortDirection === 'asc' ? numA - numB : numB - numA;
  });

  const renderSortIcon = (columnKey) => {
    if (sortColumn !== columnKey) {
      return <ArrowUpDown size={14} style={{ opacity: 0.35, marginLeft: '6px' }} />;
    }
    return sortDirection === 'asc' ? (
      <ArrowUp size={14} color="#EA580C" style={{ marginLeft: '6px' }} />
    ) : (
      <ArrowDown size={14} color="#EA580C" style={{ marginLeft: '6px' }} />
    );
  };

  const columns = [
    { key: 'model', label: 'Modelo' },
    { key: 'precision', label: 'Precision' },
    { key: 'recall', label: 'Recall' },
    { key: 'f1', label: 'F1' },
    { key: 'map50', label: 'mAP@0.50' },
    { key: 'map5095', label: 'mAP@0.50:95' },
    { key: 'fps', label: 'FPS' }
  ];

  return (
    <section className="card-section">
      <div className="section-title">
        <Table color="#F97316" size={24} />
        <span>Resultados de Rendimiento Global en Test</span>
      </div>
      <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginBottom: '16px' }}>
        Listado cuantitativo interactivo. Haz clic en las cabeceras para ordenar ascendentemente o descendentemente por cualquier columna.
      </p>

      <div className="ranking-table-container">
        <table className="ranking-table">
          <thead>
            <tr>
              {columns.map((col) => (
                <th
                  key={col.key}
                  onClick={() => handleSort(col.key)}
                  style={{ cursor: 'pointer', userSelect: 'none' }}
                  title={`Ordenar por ${col.label}`}
                >
                  <div style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                    <span>{col.label}</span>
                    {renderSortIcon(col.key)}
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sortedData.map((row, idx) => (
              <tr key={idx}>
                <td>
                  <strong style={{ color: 'var(--text-title)' }}>
                    {row.model}
                  </strong>
                </td>
                <td>{row.precision}</td>
                <td>{row.recall}</td>
                <td>{row.f1}</td>
                <td><strong>{row.map50}</strong></td>
                <td>{row.map5095}</td>
                <td>
                  <span style={{ fontWeight: 700, color: '#0F172A' }}>
                    {row.fps}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
