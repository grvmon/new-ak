import React, { useState } from 'react';

export default function Calculator() {
  const [downPaymentPercent, setDownPaymentPercent] = useState<number>(20);
  const propertyPrice = 31000000; // 3.10 Cr base price

  const downPaymentAmount = (propertyPrice * downPaymentPercent) / 100;
  const loanAmount = propertyPrice - downPaymentAmount;
  
  // Basic EMI calc: P x R x (1+R)^N / [(1+R)^N-1]
  const rate = 8.5 / 12 / 100; // 8.5% annual
  const months = 20 * 12; // 20 years
  
  const emi = loanAmount > 0 
    ? (loanAmount * rate * Math.pow(1 + rate, months)) / (Math.pow(1 + rate, months) - 1)
    : 0;

  const formatCurrency = (val: number) => {
    if (val >= 10000000) return `₹ ${(val / 10000000).toFixed(2)}Cr`;
    if (val >= 100000) return `₹ ${(val / 100000).toFixed(2)}L`;
    return `₹ ${Math.round(val).toLocaleString('en-IN')}`;
  };

  return (
    <div className="bg-white rounded-sm border-[0.5px] border-[#55555a26] p-8 max-w-lg">
      <h3 className="font-sans text-[0.85rem] uppercase tracking-widest text-[#55555A] mb-4">Yield & EMI Calculator</h3>
      <p className="font-sans text-[0.95rem] text-[#1C1C1E] mb-8">Analyze asset fundamentals and projected leverage.</p>
      
      <div className="mb-8">
        <div className="flex justify-between font-sans text-[0.85rem] mb-2">
          <span className="font-bold text-[#1C1C1E]">Down Payment</span>
          <span className="text-[#804526] font-bold">{downPaymentPercent}% ({formatCurrency(downPaymentAmount)})</span>
        </div>
        
        {/* Strict 2px track with 4px radius thumb */}
        <input 
          type="range" 
          min="10" 
          max="100" 
          step="5"
          value={downPaymentPercent} 
          onChange={(e) => setDownPaymentPercent(Number(e.target.value))}
          className="w-full"
        />
        <div className="flex justify-between font-sans text-[0.75rem] text-[#55555A] mt-2">
          <span>10%</span>
          <span>100%</span>
        </div>
      </div>
      
      <div className="border-t-[0.5px] border-[#55555a26] pt-6 flex justify-between items-end">
        <div>
          <div className="font-sans text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A] mb-1">Projected Monthly EMI</div>
          <div className="font-serif text-3xl text-[#1C1C1E]">{formatCurrency(emi)}</div>
        </div>
        <a href="#" className="font-sans text-[0.85rem] text-[#804526] underline underline-offset-4 decoration-[#804526]/30 hover:decoration-[#804526] transition-colors font-bold">
          View Schedule
        </a>
      </div>
    </div>
  );
}
