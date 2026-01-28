import { useLocation, useNavigate, Navigate } from 'react-router-dom';
import { Button } from '../components/Button';
import { Card } from '../components/Card';
import { ShieldAlert, ShieldCheck, AlertTriangle, ArrowLeft, RefreshCw, BarChart3, ScanFace } from 'lucide-react';
import { motion } from 'framer-motion';
import { cn } from '../lib/utils';

export function Result() {
    const { state } = useLocation();
    const navigate = useNavigate();

    if (!state?.result) {
        return <Navigate to="/analyzer" replace />;
    }

    const { result } = state;

    const statusConfig = {
        fraud: {
            color: 'text-brand-danger',
            bgColor: 'bg-brand-danger/10',
            borderColor: 'border-brand-danger/20',
            icon: ShieldAlert,
            label: 'Fraud Detected',
            description: 'High risk detected. This call matches known fraud patterns.'
        },
        spam: {
            color: 'text-brand-warning',
            bgColor: 'bg-brand-warning/10',
            borderColor: 'border-brand-warning/20',
            icon: AlertTriangle,
            label: 'Likely Spam',
            description: 'Suspicious patterns detected. Exercise caution.'
        },
        safe: {
            color: 'text-brand-success',
            bgColor: 'bg-brand-success/10',
            borderColor: 'border-brand-success/20',
            icon: ShieldCheck,
            label: 'Safe Call',
            description: 'No malicious patterns detected.'
        }
    };

    const config = statusConfig[result.status];
    const Icon = config.icon;

    return (
        <div className="container mx-auto px-4 py-12 min-h-[calc(100vh-4rem)]">
            <Button
                variant="ghost"
                className="mb-8 gap-2 pl-0 hover:pl-2 transition-all"
                onClick={() => navigate('/analyzer')}
            >
                <ArrowLeft className="w-4 h-4" /> Back to Analyzer
            </Button>

            <div className="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                {/* Main Result Card */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className="md:col-span-2"
                >
                    <Card className={cn("p-12 text-center border-2 relative overflow-hidden", config.borderColor)}>
                        <div className={cn(
                            "absolute inset-0 opacity-10 blur-3xl",
                            config.bgColor.replace('/10', '/30')
                        )} />

                        <div className="relative z-10 flex flex-col items-center">
                            <div className={cn(
                                "p-6 rounded-full mb-6",
                                config.bgColor,
                                config.color
                            )}>
                                <Icon className="w-16 h-16" />
                            </div>

                            <h1 className={cn("text-5xl font-bold mb-4", config.color)}>
                                {config.label}
                            </h1>

                            <p className="text-xl text-brand-muted max-w-lg mx-auto">
                                {config.description}
                            </p>
                        </div>
                    </Card>
                </motion.div>

                {/* Confidence Score */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.1 }}
                >
                    <Card className="h-full p-8 flex flex-col justify-center items-center relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-4 opacity-10">
                            <BarChart3 className="w-24 h-24" />
                        </div>
                        <h3 className="text-lg font-medium text-brand-muted mb-2">AI Confidence Score</h3>
                        <div className="relative flex items-center justify-center">
                            <svg className="w-40 h-40 transform -rotate-90">
                                <circle cx="80" cy="80" r="70" stroke="currentColor" strokeWidth="10" fill="transparent" className="text-brand-muted/20" />
                                <circle
                                    cx="80"
                                    cy="80"
                                    r="70"
                                    stroke="currentColor"
                                    strokeWidth="10"
                                    fill="transparent"
                                    strokeDasharray={440}
                                    strokeDashoffset={440 - (440 * result.confidence)}
                                    className={cn(config.color, "transition-all duration-1000 ease-out")}
                                    strokeLinecap="round"
                                />
                            </svg>
                            <span className="absolute text-4xl font-bold text-white">
                                {Math.round(result.confidence * 100)}%
                            </span>
                        </div>
                    </Card>
                </motion.div>

                {/* Analysis Details */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2 }}
                >
                    <Card className="h-full p-8 relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-4 opacity-10">
                            <ScanFace className="w-24 h-24" />
                        </div>
                        <h3 className="text-lg font-medium text-brand-muted mb-6">Analysis Details</h3>

                        <div className="space-y-6">
                            <div>
                                <div className="text-sm text-brand-muted mb-2">Detected Tone</div>
                                <div className="inline-block px-3 py-1 rounded-full bg-white/5 border border-white/10 text-white font-medium">
                                    {result.tone}
                                </div>
                            </div>

                            <div>
                                <div className="text-sm text-brand-muted mb-2">Flagged Keywords</div>
                                <div className="flex flex-wrap gap-2">
                                    {result.keywords.map((keyword, i) => (
                                        <span
                                            key={i}
                                            className="px-2 py-1 rounded-md bg-brand-primary/10 border border-brand-primary/20 text-brand-primary text-sm"
                                        >
                                            {keyword}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </Card>
                </motion.div>

                <div className="md:col-span-2 flex justify-center mt-8">
                    <Button
                        onClick={() => navigate('/analyzer')}
                        size="lg"
                        className="gap-2"
                    >
                        <RefreshCw className="w-4 h-4" /> Analyze Another Call
                    </Button>
                </div>

            </div>
        </div>
    );
}
