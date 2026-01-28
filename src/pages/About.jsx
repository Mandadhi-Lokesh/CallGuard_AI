import { Card } from '../components/Card';
import { motion } from 'framer-motion';
import { ArrowDown, HeartHandshake, Building2, Smartphone, Shield, Users, Lock } from 'lucide-react';

export function About() {
    const impacts = [
        {
            icon: Users,
            title: "Protecting Senior Citizens",
            description: "Elderly users are the most vulnerable targets. Our AI acts as a dedicated guardian, alerting them to family emergency scams and impersonation attempts instantly."
        },
        {
            icon: Building2,
            title: "Banking Fraud Prevention",
            description: "We detect OTP requests, 'KYC update' scams, and account blocking threats in real-time, preventing financial loss before it happens."
        },
        {
            icon: Smartphone,
            title: "Telecom Network Safety",
            description: "Partnering with telecom providers to identify and block massive robo-calling operations at the source, effectively cleaning the network."
        },
        {
            icon: Shield,
            title: "National Security",
            description: "Identifying coordinated disinformation campaigns and security threats through advanced pattern matching across the network."
        },
        {
            icon: HeartHandshake,
            title: "Trust in Communication",
            description: "Restoring faith in voice calls. When your phone rings, you shouldn't have to wonder if it's a trap."
        },
        {
            icon: Lock,
            title: "Privacy First",
            description: "Our technology is designed with privacy at its core. Processing happens securely, and no personal conversations are stored."
        }
    ];

    return (
        <div className="container mx-auto px-4 py-16">
            <div className="max-w-3xl mx-auto text-center mb-16 space-y-4">
                <h1 className="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-brand-accent to-white">
                    Our Impact
                </h1>
                <p className="text-xl text-brand-muted">
                    We are building a safer digital India by stopping fraud at the source.
                </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {impacts.map((item, index) => (
                    <motion.div
                        key={index}
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: index * 0.1 }}
                    >
                        <Card className="h-full p-8 hover:bg-brand-card/50 transition-colors border-white/5 group">
                            <div className="mb-6 p-3 rounded-lg bg-brand-primary/10 w-fit group-hover:bg-brand-primary/20 transition-colors">
                                <item.icon className="w-8 h-8 text-brand-accent" />
                            </div>
                            <h3 className="text-xl font-semibold mb-3 text-white">
                                {item.title}
                            </h3>
                            <p className="text-brand-muted leading-relaxed">
                                {item.description}
                            </p>
                        </Card>
                    </motion.div>
                ))}
            </div>



            <section className="mt-24 mb-24">
                <h2 className="text-3xl font-bold mb-8 text-center text-white">Our Technology</h2>
                <div className="bg-brand-card/50 border border-white/5 rounded-3xl p-8 md:p-12">
                    <div className="grid md:grid-cols-2 gap-12 items-center">
                        <div>
                            <h3 className="text-2xl font-bold mb-4 text-white">AI Detection Logic</h3>
                            <p className="text-brand-muted mb-6 text-lg">
                                The system currently uses a rule-based and pattern-driven inference approach designed to approximate real-world AI decision-making behavior:
                            </p>
                            <ul className="space-y-4">
                                {[
                                    "Keyword and phrase risk scoring",
                                    "Urgency and threat detection",
                                    "Aggregated confidence calculation",
                                    "Risk categorization (High / Medium / Low)"
                                ].map((item, i) => (
                                    <li key={i} className="flex items-center gap-3 text-brand-muted">
                                        <span className="w-2 h-2 rounded-full bg-brand-accent"></span>
                                        {item}
                                    </li>
                                ))}
                            </ul>
                        </div>
                        <div className="bg-black/40 rounded-2xl p-6 border border-white/5 font-mono text-sm text-brand-accent/80">
                            <div className="mb-2 text-brand-muted/50 border-b border-white/5 pb-2">Analysis Pipeline</div>
                            <div className="space-y-3">
                                <div className="flex items-center gap-2">
                                    <span className="text-white">1. Input:</span> Raw Audio (.wav/.mp3)
                                </div>
                                <div className="flex justify-center"><ArrowDown className="w-4 h-4 opacity-50" /></div>
                                <div className="flex items-center gap-2">
                                    <span className="text-white">2. Process:</span> Feature Extraction
                                </div>
                                <div className="flex justify-center"><ArrowDown className="w-4 h-4 opacity-50" /></div>
                                <div className="flex items-center gap-2">
                                    <span className="text-white">3. Logic:</span> Inference Engine
                                </div>
                                <div className="flex justify-center"><ArrowDown className="w-4 h-4 opacity-50" /></div>
                                <div className="flex items-center gap-2">
                                    <span className="text-white">4. Output:</span> JSON Risk Profile
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section className="mt-24 text-center">
                <div className="p-12 rounded-3xl bg-gradient-to-b from-brand-card to-transparent border border-white/5">
                    <h2 className="text-3xl font-bold mb-6">Why It Matters</h2>
                    <div className="grid md:grid-cols-3 gap-8 text-center">
                        <Stat value="₹1,000 Cr+" label="Saved in Potential Losses" />
                        <Stat value="50M+" label="Calls Analyze Daily" />
                        <Stat value="99.9%" label="Detection Accuracy" />
                    </div>
                </div>
            </section>

            <section className="mt-24">
                <h2 className="text-3xl font-bold mb-8 text-center text-white">Future Scope</h2>
                <div className="grid md:grid-cols-2 gap-6">
                    <Card className="p-6 border-brand-primary/20 bg-brand-primary/5">
                        <div className="flex items-start gap-4">
                            <div className="p-3 bg-brand-accent/10 rounded-lg text-brand-accent">
                                <Smartphone className="w-6 h-6" />
                            </div>
                            <div>
                                <h3 className="text-xl font-semibold mb-2 text-white">Real-Time Call Integration</h3>
                                <p className="text-brand-muted">Integrating with Android/iOS dialers (via API) to provide live warnings as the call happens, not just post-call analysis.</p>
                            </div>
                        </div>
                    </Card>

                    <Card className="p-6 border-brand-primary/20 bg-brand-primary/5">
                        <div className="flex items-start gap-4">
                            <div className="p-3 bg-brand-accent/10 rounded-lg text-brand-accent">
                                <Building2 className="w-6 h-6" />
                            </div>
                            <div>
                                <h3 className="text-xl font-semibold mb-2 text-white">Multilingual Support</h3>
                                <p className="text-brand-muted">Expanding our NLP models to support Hindi, Tamil, Telugu, and other regional Indian languages for deeper penetration.</p>
                            </div>
                        </div>
                    </Card>

                    <Card className="p-6 border-brand-primary/20 bg-brand-primary/5">
                        <div className="flex items-start gap-4">
                            <div className="p-3 bg-brand-accent/10 rounded-lg text-brand-accent">
                                <Shield className="w-6 h-6" />
                            </div>
                            <div>
                                <h3 className="text-xl font-semibold mb-2 text-white">Advanced ML Models</h3>
                                <p className="text-brand-muted">Replacing current heuristic logic with Transformer-based models (BERT/Whisper) for higher nuance detection.</p>
                            </div>
                        </div>
                    </Card>

                    <Card className="p-6 border-brand-primary/20 bg-brand-primary/5">
                        <div className="flex items-start gap-4">
                            <div className="p-3 bg-brand-accent/10 rounded-lg text-brand-accent">
                                <HeartHandshake className="w-6 h-6" />
                            </div>
                            <div>
                                <h3 className="text-xl font-semibold mb-2 text-white">Telecom Partnership</h3>
                                <p className="text-brand-muted">API-level integration with major telecom providers to screen calls at the network level before they reach the user.</p>
                            </div>
                        </div>
                    </Card>
                </div>
            </section>
        </div >
    );
}

function Stat({ value, label }) {
    return (
        <div className="space-y-2">
            <div className="text-4xl md:text-5xl font-bold text-white">{value}</div>
            <div className="text-brand-accent font-medium">{label}</div>
        </div>
    );
}
