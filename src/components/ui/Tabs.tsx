import React, { useState, useRef } from 'react';

interface TabItem {
  id: string;
  label: string;
  content: React.ReactNode;
}

interface TabsProps {
  items: TabItem[];
  defaultTabId?: string;
  className?: string;
}

export default function Tabs({ items, defaultTabId, className = '' }: TabsProps) {
  const [activeTab, setActiveTab] = useState(defaultTabId || items[0]?.id);
  const tabRefs = useRef<(HTMLButtonElement | null)[]>([]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLButtonElement>, index: number) => {
    let newIndex = index;
    if (e.key === 'ArrowRight') {
      newIndex = index === items.length - 1 ? 0 : index + 1;
    } else if (e.key === 'ArrowLeft') {
      newIndex = index === 0 ? items.length - 1 : index - 1;
    } else if (e.key === 'Home') {
      newIndex = 0;
    } else if (e.key === 'End') {
      newIndex = items.length - 1;
    }

    if (newIndex !== index) {
      e.preventDefault();
      setActiveTab(items[newIndex].id);
      tabRefs.current[newIndex]?.focus();
    }
  };

  return (
    <div className={`w-full ${className}`}>
      <div
        role="tablist"
        aria-label="Content Tabs"
        className="flex space-x-8 border-b-[0.5px] border-[#55555a26] mb-6"
      >
        {items.map((item, index) => {
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              ref={(el) => (tabRefs.current[index] = el)}
              role="tab"
              aria-selected={isActive}
              aria-controls={`tabpanel-${item.id}`}
              id={`tab-${item.id}`}
              tabIndex={isActive ? 0 : -1}
              onClick={() => setActiveTab(item.id)}
              onKeyDown={(e) => handleKeyDown(e, index)}
              className={`pb-4 border-b-2 font-sans text-[0.85rem] font-bold uppercase tracking-[0.05em] transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#804526] focus-visible:ring-offset-2 ${
                isActive
                  ? 'border-[#804526] text-[#804526]'
                  : 'border-transparent text-[#55555A] hover:text-[#804526]'
              }`}
            >
              {item.label}
            </button>
          );
        })}
      </div>

      {items.map((item) => (
        <div
          key={item.id}
          id={`tabpanel-${item.id}`}
          role="tabpanel"
          aria-labelledby={`tab-${item.id}`}
          hidden={activeTab !== item.id}
          tabIndex={0}
          className="font-sans text-[0.95rem] text-[#1C1C1E] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#804526]"
        >
          {item.content}
        </div>
      ))}
    </div>
  );
}
