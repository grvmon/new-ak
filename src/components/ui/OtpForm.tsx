import React, { useState } from 'react';

export default function OtpForm() {
  const [step, setStep] = useState<1 | 2>(1);
  const [phone, setPhone] = useState('');
  const [otp, setOtp] = useState('');

  return (
    <div className="bg-white rounded-sm border-[0.5px] border-[#55555a26] p-8 max-w-md">
      <h3 className="font-sans text-lg text-[#1C1C1E] mb-6">Concierge Advisory Form</h3>
      
      {step === 1 && (
        <div className="space-y-6">
          <div>
            <div className="font-sans text-[0.75rem] uppercase tracking-widest text-[#55555A] mb-4">Step 1: Secure Entry</div>
            <div className="relative">
              <span className="absolute left-0 bottom-3 font-sans text-[0.95rem] text-[#1C1C1E] font-bold">+91</span>
              <input 
                type="tel" 
                className="w-full border-b-[0.5px] border-[#55555a4d] pl-10 pb-3 focus:outline-none focus:border-[#804526] transition-colors text-[0.95rem] bg-transparent"
                placeholder="Enter your mobile number"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
              />
            </div>
          </div>
          <button 
            type="button" 
            onClick={() => setPhone && setStep(2)}
            className="w-full bg-[#1C1C1E] text-white font-bold py-3 text-[0.85rem] uppercase tracking-widest rounded-sm hover:bg-[#804526] transition-colors"
          >
            Authenticate
          </button>
        </div>
      )}

      {step === 2 && (
        <div className="space-y-6">
          <div>
            <div className="font-sans text-[0.75rem] uppercase tracking-widest text-[#55555A] mb-4">Step 2: Verification</div>
            <input 
              type="text" 
              className="w-full border-b-[0.5px] border-[#55555a4d] pb-3 focus:outline-none focus:border-[#804526] transition-colors text-[0.95rem] tracking-[0.5em] text-center font-bold bg-transparent"
              placeholder="• • • • • •"
              maxLength={6}
              value={otp}
              onChange={(e) => setOtp(e.target.value)}
            />
          </div>
          <div className="flex justify-between items-center">
            <button 
              type="button" 
              onClick={() => setStep(1)}
              className="text-[#55555A] text-[0.85rem] underline underline-offset-4 hover:text-[#1C1C1E] transition-colors"
            >
              Back
            </button>
            <button 
              type="button" 
              className="text-[#804526] text-[0.85rem] font-bold hover:opacity-80 transition-opacity"
            >
              Resend Code
            </button>
          </div>
          <button 
            type="button" 
            className="w-full bg-[#804526] text-white font-bold py-3 text-[0.85rem] uppercase tracking-widest rounded-sm hover:bg-[#1C1C1E] transition-colors"
          >
            Request Advisory Call
          </button>
        </div>
      )}
    </div>
  );
}
