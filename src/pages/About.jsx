import { Card } from '../components/Card';
import { motion } from 'framer-motion';
import { HeartHandshake, Building2, Smartphone, Shield, Users, Lock } from 'lucide-react';

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
        </div>
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
