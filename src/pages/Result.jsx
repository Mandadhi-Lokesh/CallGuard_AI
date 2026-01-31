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
        <div className="container mx-auto px-4 py-8 min-h-[calc(100vh-4rem)]">
            <div className="flex items-center justify-between mb-8">
                <Button
                    variant="ghost"
                    className="gap-2 pl-0 hover:pl-2 transition-all"
                    onClick={() => navigate('/analyzer')}
                >
                    <ArrowLeft className="w-4 h-4" /> New Assessment
                </Button>
                {result.robustness_applied && (
                    <div className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-brand-muted text-xs font-medium">
                        Stress Test Mode
                    </div>
                )}
            </div>

            <div className="grid md:grid-cols-12 gap-6 max-w-6xl mx-auto">
                {/* 1. Main Assessment Card */}
                <div className="md:col-span-8">
                    <Card className={cn("h-full p-8 relative overflow-hidden flex flex-col justify-center", config.borderColor)}>
                        <div className={cn(
                            "absolute inset-0 opacity-10 blur-3xl",
                            config.bgColor.replace('/10', '/30')
                        )} />

                        <div className="relative z-10">
                            <div className="flex items-center gap-2 mb-6">
                                <ScanFace className="w-5 h-5 text-brand-muted" />
                                <span className="text-sm uppercase tracking-widest text-brand-muted font-medium">Assessment Result</span>
                            </div>

                            <div className="flex items-start gap-6">
                                <div className={cn("p-4 rounded-2xl shrink-0", config.bgColor, config.color)}>
                                    <Icon className="w-12 h-12" />
                                </div>
                                <div>
                                    <h1 className={cn("text-4xl font-bold mb-2", config.color)}>
                                        {config.label}
                                    </h1>
                                    <p className="text-lg text-brand-muted mb-4 leading-relaxed">
                                        {config.description}
                                    </p>

                                    <div className="flex items-center gap-2 text-xs text-brand-muted bg-black/20 p-2 rounded border border-white/5">
                                        <Info className="w-3 h-3" />
                                        This system performs deep acoustic testing to assess whether a voice exhibits synthetic or human speech behavior.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </Card>
                </div>

                {/* 2. Key Metrics (Top Right) */}
                <div className="md:col-span-4">
                    <Card className="h-full p-6 space-y-6">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2">
                                <Activity className="w-5 h-5 text-brand-accent" />
                                <h3 className="font-semibold text-white">Acoustic Evidence</h3>
                            </div>
                            <div className="text-xs text-brand-muted text-right">
                                <div>Confidence Level: {(result.confidence * 100).toFixed(0)}%</div>
                                <div className="text-[10px] opacity-70 mt-1">Confidence reflects strength of acoustic evidence.</div>
                            </div>
                        </div>

                        {signals ? (
                            <div className="space-y-4">
                                <SignalBar
                                    label="Pitch Dynamics"
                                    value={signals.pitch_variance.value}
                                    interpretation={signals.pitch_variance.interpretation}
                                />
                                <SignalBar
                                    label="Vocal Jitter"
                                    value={signals.jitter.value}
                                    interpretation={signals.jitter.interpretation}
                                    inverse
                                />
                                <SignalBar
                                    label="Spectral Grade"
                                    value={signals.spectral_flatness.value}
                                    interpretation={signals.spectral_flatness.interpretation}
                                    inverse
                                />
                            </div>
                        ) : (
                            <div className="h-20 flex items-center justify-center text-sm text-brand-muted italic">
                                Signal data unavailable
                            </div>
                        )}
                    </Card>
                </div>

                {/* 3. Explanation & Logic (Bottom) */}
                <div className="md:col-span-12">
                    <Card className="p-8 border-white/10 bg-white/5">
                        <h3 className="text-lg font-semibold mb-4 text-white">Analysis Findings</h3>
                        <div className="grid md:grid-cols-2 gap-8">
                            <div>
                                <h4 className="text-xs uppercase tracking-wider text-brand-muted mb-3">Primary Indicators</h4>
                                <ul className="space-y-3">
                                    {result.explanation ? result.explanation.map((item, index) => (
                                        <li key={index} className="flex items-start gap-3 text-brand-muted leading-relaxed text-sm">
                                            <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-brand-accent shrink-0" />
                                            {item}
                                        </li>
                                    )) : (
                                        <li className="text-brand-muted">Processing...</li>
                                    )}
                                </ul>
                            </div>

                            <div>
                                <h4 className="text-xs uppercase tracking-wider text-brand-muted mb-3">Temporal Stability</h4>
                                {chunk_analysis?.chunk_confidence && chunk_analysis.chunk_confidence.length > 0 ? (
                                    <div className="h-24 w-full relative border-l border-b border-white/10">
                                        {/* Simple SVG Line Chart */}
                                        <svg className="w-full h-full overflow-visible" preserveAspectRatio="none">
                                            <polyline
                                                fill="none"
                                                stroke="currentColor"
                                                strokeWidth="2"
                                                className="text-brand-accent"
                                                points={chunk_analysis.chunk_confidence.map((score, i, arr) => {
                                                    const x = (i / (arr.length - 1)) * 100;
                                                    const y = 100 - score; // Invert for Y-axis (0 at top)
                                                    return `${x},${y}`;
                                                }).join(' ')}
                                                vectorEffect="non-scaling-stroke"
                                            />
                                        </svg>
                                        <div className="absolute -bottom-4 left-0 text-[10px] text-brand-muted">Start</div>
                                        <div className="absolute -bottom-4 right-0 text-[10px] text-brand-muted">End</div>
                                    </div>
                                ) : (
                                    <div className="h-24 flex items-center justify-center border border-dashed border-white/10 rounded">
                                        <span className="text-xs text-brand-muted">Timeline unavailable</span>
                                    </div>
                                )}
                                <p className="text-xs text-brand-muted mt-6 text-right">
                                    {chunk_analysis?.trend === 'fluctuating' ? 'Warning: High Instability Detected' : 'Signal Stability: Consistent'}
                                </p>
                            </div>
                        </div>
                    </Card>
                </div>
            </div>
        </div>
    );
}
