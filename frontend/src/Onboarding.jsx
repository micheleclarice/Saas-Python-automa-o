import { useEffect, useState } from "react";

export default function Onboarding({ token }) {
  const [step, setStep] = useState(1);

  useEffect(() => {
    fetch("http://localhost:8000/onboarding", {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(data => setStep(data?.step || 1));
  }, []);

  const next = async () => {
    const res = await fetch("http://localhost:8000/onboarding/next", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` }
    });

    const data = await res.json();
    setStep(data.step);
  };

  return (
    <div>
      <h2>Onboarding Step {step}</h2>

      {step === 1 && <p>Conecte seu WhatsApp</p>}
      {step === 2 && <p>Crie sua primeira campanha</p>}
      {step === 3 && <p>Ative seu agente de vendas</p>}

      <button onClick={next}>Próximo</button>
    </div>
  );
}