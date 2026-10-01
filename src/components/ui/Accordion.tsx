import React, { useState, useRef, useEffect } from 'react';

interface AccordionItem {
  id: string;
  title: string;
  content: React.ReactNode;
}

interface AccordionProps {
  items: AccordionItem[];
  allowMultiple?: boolean;
  className?: string;
}

export default function Accordion({ items, allowMultiple = false, className = '' }: AccordionProps) {
  const [expandedIds, setExpandedIds] = useState<Set<string>>(new Set());

  const toggle = (id: string) => {
    setExpandedIds((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(id)) {
        newSet.delete(id);
      } else {
        if (!allowMultiple) {
          newSet.clear();
        }
        newSet.add(id);
      }
      return newSet;
    });
  };

  return (
    <div className={`w-full ${className}`}>
      {items.map((item) => {
        const isExpanded = expandedIds.has(item.id);
        const buttonId = `accordion-button-${item.id}`;
        const panelId = `accordion-panel-${item.id}`;

        return (
          <div key={item.id} className="border-b-[0.5px] border-[#55555a26]">
            <h3>
              <button
                type="button"
                id={buttonId}
                aria-expanded={isExpanded}
                aria-controls={panelId}
                onClick={() => toggle(item.id)}
                className="w-full flex justify-between items-center py-6 text-left cursor-pointer bg-transparent transition-colors hover:text-[#804526] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#804526]"
              >
                <span className="font-sans text-[0.95rem] font-bold text-[#1C1C1E]">{item.title}</span>
                <span className="text-[#55555A] font-serif text-xl" aria-hidden="true">
                  {isExpanded ? '−' : '+'}
                </span>
              </button>
            </h3>
            <div
              id={panelId}
              role="region"
              aria-labelledby={buttonId}
              hidden={!isExpanded}
              className={`overflow-hidden transition-all duration-400 ease-out ${isExpanded ? 'opacity-100' : 'opacity-0'}`}
            >
              <div className="pb-6 font-sans text-[0.95rem] text-[#55555A] leading-relaxed">
                {item.content}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
