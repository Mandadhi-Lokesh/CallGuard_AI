import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FileUploader } from '../components/FileUploader';
import { Button } from '../components/Button';
import { Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

export function Analyzer() {
    const [file, setFile] = useState(null);
    const [isAnalyzing, setIsAnalyzing] = useState(false);
    const navigate = useNavigate();

    const handleAnalyze = async () => {
        if (!file) return;

        setIsAnalyzing(true);

        // Simulate API call
        setTimeout(() => {
            setIsAnalyzing(false);
            // Navigate to result with mock data
            // In a real app, we would pass the ID or data
            const mockResult = {
                status: 'fraud', // fraud, spam, safe
                confidence: 0.98,
                keywords: ['bank account', 'verify', 'otp', 'urgent', 'block'],
                tone: 'Aggressive',
                fileName: file.name
            };
            // Randomize result for demo purposes
            const rand = Math.random();
            if (rand > 0.6) {
                mockResult.status = 'safe';
                mockResult.confidence = 0.92;
                mockResult.keywords = ['delivery', 'package', 'gate'];
                mockResult.tone = 'Neutral';
            } else if (rand > 0.3) {
                mockResult.status = 'spam';
                mockResult.confidence = 0.85;
                mockResult.keywords = ['loan', 'offer', 'credit card'];
                mockResult.tone = 'Persuasive';
            }

            navigate('/result', { state: { result: mockResult } });
        }, 3000); // 3 seconds delay
    };

    return (
        <div className="container mx-auto px-4 py-16 flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="w-full max-w-2xl space-y-8 text-center"
            >
                <div className="space-y-4">
                    <h1 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-white/60">
                        Call Analyzer
                    </h1>
                    <p className="text-brand-muted text-lg">
                        Upload your call recording to detect potential fraud or spam using our advanced AI models.
                    </p>
                </div>

                <div className="py-8">
                    <FileUploader onFileSelect={setFile} />
                </div>

                <div className="flex justify-center h-16">
                    {/* Fixed height to prevent jump */}
                    {isAnalyzing ? (
                        <div className="flex flex-col items-center gap-3 text-brand-accent">
                            <Loader2 className="w-8 h-8 animate-spin" />
                            <span className="text-sm font-medium animate-pulse">Analyzing audio patterns...</span>
                        </div>
                    ) : (
                        file && (
                            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>
                                <Button
                                    className="w-48 text-lg py-6 shadow-brand-primary/25 shadow-lg"
                                    onClick={handleAnalyze}
                                >
                                    Analyze Call
                                </Button>
                            </motion.div>
                        )
                    )}
                </div>
            </motion.div>
        </div>
    );
}
