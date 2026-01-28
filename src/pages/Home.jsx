import { Link } from 'react-router-dom';
import { Button } from '../components/Button';
import { Card } from '../components/Card';
import { motion } from 'framer-motion';
import { UploadCloud, Activity, ShieldCheck, ArrowRight } from 'lucide-react';

export function Home() {
    const container = {
        hidden: { opacity: 0 },
        show: {
            opacity: 1,
            transition: {
                staggerChildren: 0.1
            }
        }
    };

    const item = {
        hidden: { opacity: 0, y: 20 },
        show: { opacity: 1, y: 0 }
    };

    return (
        <div className="flex flex-col min-h-[calc(100vh-4rem)]">
            {/* Hero Section */}
            <section className="relative flex flex-col items-center justify-center flex-1 py-20 px-4 text-center overflow-hidden">
                {/* Abstract Background Glow */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-brand-primary/20 opacity-20 blur-[120px] rounded-full pointer-events-none" />

                <motion.div
                    variants={container}
                    initial="hidden"
                    animate="show"
                    className="relative z-10 max-w-4xl mx-auto space-y-8"
                >
                    <motion.div variants={item} className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-primary/10 border border-brand-primary/20 text-brand-accent text-sm font-medium">
                        <span className="relative flex h-2 w-2">
                            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-brand-accent opacity-75"></span>
                            <span className="relative inline-flex rounded-full h-2 w-2 bg-brand-accent"></span>
                        </span>
                        Live Fraud Detection System
                    </motion.div>

                    <motion.h1 variants={item} className="text-5xl md:text-7xl font-bold tracking-tight text-white">
                        AI-Powered <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-accent to-blue-400">Call Fraud</span> Detection
                    </motion.h1>

                    <motion.p variants={item} className="text-lg md:text-xl text-brand-muted max-w-2xl mx-auto leading-relaxed">
                        Protecting India's digital ecosystem. Our advanced AI analyzes speech patterns and call metadata to instantly detect scam and spam calls with high accuracy.
                    </motion.p>

                    <motion.div variants={item} className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
                        <Link to="/analyzer">
                            <Button size="lg" className="w-full sm:w-auto gap-2">
                                Analyze Call Audio <ArrowRight className="w-4 h-4" />
                            </Button>
                        </Link>
                        <Link to="/about">
                            <Button variant="secondary" size="lg" className="w-full sm:w-auto">
                                Learn How It Works
                            </Button>
                        </Link>
                    </motion.div>
                </motion.div>
            </section>

            {/* How It Works Section */}
            <section className="py-24 bg-black/20">
                <div className="container mx-auto px-4">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="text-center mb-16"
                    >
                        <h2 className="text-3xl font-bold mb-4">How It Works</h2>
                        <p className="text-brand-muted">Three simple steps to verify call safety</p>
                    </motion.div>

                    <div className="grid md:grid-cols-3 gap-8">
                        <StepCard
                            icon={<UploadCloud className="w-10 h-10 text-brand-accent" />}
                            title="1. Audio Upload"
                            description="Securely ingest .wav or .mp3 files. Audio is pre-processed and normalized for consistent analysis."
                            delay={0.1}
                        />
                        <StepCard
                            icon={<Activity className="w-10 h-10 text-brand-accent" />}
                            title="2. Feature Extraction"
                            description="Our model extracts key acoustic features, tone patterns, and keyword density from the raw audio data."
                            delay={0.2}
                        />
                        <StepCard
                            icon={<ShieldCheck className="w-10 h-10 text-brand-accent" />}
                            title="3. Risk Classification"
                            description="The AI engine classifies the call as Fraud, Spam, or Safe with a confidence score and explainable risk factors."
                            delay={0.3}
                        />
                    </div>
                </div>
            </section>
        </div>
    );
}

function StepCard({ icon, title, description, delay }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay }}
        >
            <Card className="h-full flex flex-col items-center text-center p-8 hover:border-brand-accent/50 transition-colors group">
                <div className="mb-6 p-4 rounded-2xl bg-brand-primary/10 group-hover:bg-brand-primary/20 transition-colors">
                    {icon}
                </div>
                <h3 className="text-xl font-semibold mb-3">{title}</h3>
                <p className="text-brand-muted leading-relaxed">
                    {description}
                </p>
            </Card>
        </motion.div>
    );
}
