import { useLocation, useNavigate, Navigate } from 'react-router-dom';
import { Button } from '../components/Button';
import { Card } from '../components/Card';
import { ShieldAlert, ShieldCheck, AlertTriangle, ArrowLeft, RefreshCw, BarChart3, ScanFace, Activity, Info } from 'lucide-react';
import { motion } from 'framer-motion';
import { cn } from '../lib/utils';

const SignalBar = ({ label, value, interpretation, inverse = false }) => {
    // Basic normalization for display
    let percent = 50;
    if (label.includes('Pitch')) percent = Math.min(value / 500, 1) * 100;
    else if (label.includes('Jitter')) percent = Math.min(value / 0.1, 1) * 100;
    else if (label.includes('Flatness')) percent = value * 100;

    return (
        <div className="space-y-1">
            <div className="flex justify-between text-xs">
                <span className="text-brand-muted uppercase tracking-wider">{label}</span>
                <span className={cn("font-medium", "text-white")}>
                    {interpretation}
                </span>
            </div>
            <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
                <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${percent}%` }}
                    className="h-full rounded-full bg-brand-accent/70"
                />
            </div>
        </div>
    );
};

export function Result() {
    const { state } = useLocation();
    const navigate = useNavigate();

    if (!state?.result) {
        return <Navigate to="/analyzer" replace />;
    }

    const { result, useCase } = state;
    // Fallback if backend doesn't send them (e.g. if user is running old backend instance)
    const { signals, chunk_analysis } = result;

    const statusConfig = {
        fraud: {
            color: 'text-brand-danger',
            bgColor: 'bg-brand-danger/10',
            borderColor: 'border-brand-danger/20',
            icon: ShieldAlert,
            label: 'Synthetic Voice Signature',
            description: 'Audio properties exhibit definite synthetic generation patterns.'
        },
        spam: {
            color: 'text-brand-warning',
            bgColor: 'bg-brand-warning/10',
            borderColor: 'border-brand-warning/20',
            icon: AlertTriangle,
            label: 'Mixed Acoustic Signals',
            description: 'Verification returned conflicting signal data. Acoustic evidence is inconclusive.'
        },
        safe: {
            color: 'text-brand-success',
            bgColor: 'bg-brand-success/10',
            borderColor: 'border-brand-success/20',
            icon: ShieldCheck,
            label: 'Human Voice Signature',
            description: 'Audio properties are consistent with human vocal physics.'
        }
    };

    const config = statusConfig[result.status] || statusConfig['safe'];
    const Icon = config.icon;

    return (
        <div className="container mx-auto px-4 py-8 min-h-[calc(100vh-4rem)] flex flex-col items-center justify-center">
            <Card className="max-w-xl w-full p-8 border-white/10 bg-white/5 space-y-6">
                <div className="analysis-result space-y-6">
                    <h2 className="text-2xl font-bold text-center mb-6">Analysis Result</h2>

                    <div className="text-center">
                        <h3 className={cn(
                            "text-3xl font-bold mb-2",
                            result.status === "AI" ? "text-brand-danger" : "text-brand-success"
                        )}>
                            Status: {result.status}
                        </h3>
                        <p className="text-xl text-brand-muted">
                            <strong>Confidence:</strong> {result.confidence}%
                        </p>
                    </div>

                    <div className="bg-black/20 p-6 rounded-lg border border-white/5">
                        <p className="font-semibold mb-3 text-brand-muted uppercase text-sm tracking-wider">Classified based on:</p>
                        <ul className="space-y-2">
                            {result.classified_based_on && result.classified_based_on.map((item, idx) => (
                                <li key={idx} className="flex items-start gap-2 text-brand-muted">
                                    <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-brand-accent shrink-0" />
                                    {item}
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>

                <Button
                    variant="outline"
                    className="w-full mt-8"
                    onClick={() => navigate('/analyzer')}
                >
                    Analyze Another File
                </Button>
            </Card>
        </div>
    );
}
