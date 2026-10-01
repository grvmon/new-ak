import React, { useState } from 'react';

interface GalleryProps {
  images: { src: string; alt: string }[];
  title: string;
}

export default function Gallery({ images, title }: GalleryProps) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const next = () => setCurrentIndex((prev) => (prev === images.length - 1 ? 0 : prev + 1));
  const prev = () => setCurrentIndex((prev) => (prev === 0 ? images.length - 1 : prev - 1));

  if (!images || images.length === 0) return null;

  return (
    <div className="relative w-full rounded-[4px] overflow-hidden group bg-[#1C1C1E]">
      {/* Main Image with strict 16:9 cinematic aspect ratio */}
      <div className="relative aspect-video w-full">
        <img 
          src={images[currentIndex].src} 
          alt={images[currentIndex].alt} 
          className="w-full h-full object-cover transition-opacity duration-600"
          style={{ filter: 'saturate(0.85) contrast(1.05)' }} 
        />
        
        {/* Dual Anchored Gradient */}
        <div className="absolute inset-0 pointer-events-none" style={{
          background: `
            linear-gradient(to bottom, rgba(28, 28, 30, 0.8) 0%, transparent 20%),
            linear-gradient(to top, rgba(28, 28, 30, 0.95) 0%, rgba(28, 28, 30, 0.4) 30%, transparent 100%)
          `
        }}></div>

        {/* Top Controls */}
        <div className="absolute top-6 left-6 right-6 flex justify-between items-center z-10 text-white">
          <h3 className="font-serif text-xl tracking-tight">{title}</h3>
          <div className="font-sans text-[0.85rem] tracking-widest opacity-80">
            {String(currentIndex + 1).padStart(2, '0')}/{String(images.length).padStart(2, '0')}
          </div>
        </div>

        {/* Bottom Controls */}
        <div className="absolute bottom-6 left-6 right-6 flex justify-between items-end z-10">
          <button className="font-sans text-[0.85rem] font-bold text-white hover:text-[#e5b899] transition-colors underline underline-offset-4 decoration-white/30 hover:decoration-[#e5b899]">
            View gallery
          </button>
          
          {/* Navigation Arrows with strict 4px geometry */}
          <div className="flex gap-2">
            <button 
              onClick={prev}
              className="w-10 h-10 border-[0.5px] border-white/30 rounded-[4px] flex items-center justify-center bg-white/10 backdrop-blur-md hover:bg-white/20 transition-all text-white"
              aria-label="Previous image"
            >
              ←
            </button>
            <button 
              onClick={next}
              className="w-10 h-10 border-[0.5px] border-white/30 rounded-[4px] flex items-center justify-center bg-white/10 backdrop-blur-md hover:bg-white/20 transition-all text-white"
              aria-label="Next image"
            >
              →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
