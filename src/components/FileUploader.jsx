import { useCallback, useState } from 'react';
import { cn } from '../lib/utils';
import { UploadCloud, FileAudio, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export function FileUploader({ onFileSelect }) {
    const [dragActive, setDragActive] = useState(false);
    const [selectedFile, setSelectedFile] = useState(null);

    const handleDrag = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.type === "dragenter" || e.type === "dragover") {
            setDragActive(true);
        } else if (e.type === "dragleave") {
            setDragActive(false);
        }
    }, []);

    const handleDrop = useCallback((e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragActive(false);
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFile(e.dataTransfer.files[0]);
        }
    }, []);

    const handleChange = (e) => {
        e.preventDefault();
        if (e.target.files && e.target.files[0]) {
            handleFile(e.target.files[0]);
        }
    };

    const handleFile = (file) => {
        if (file.type.startsWith('audio/') || file.name.endsWith('.wav') || file.name.endsWith('.mp3')) {
            setSelectedFile(file);
            onFileSelect(file);
        } else {
            alert("Please upload an audio file (.mp3 or .wav)");
        }
    };

    const removeFile = () => {
        setSelectedFile(null);
        onFileSelect(null);
    };

    return (
        <div className="w-full max-w-xl mx-auto">
            <AnimatePresence mode='wait'>
                {!selectedFile ? (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.95 }}
                        key="upload-zone"
                    >
                        <label
                            className={cn(
                                "relative flex flex-col items-center justify-center w-full h-80 rounded-3xl border-2 border-dashed transition-all duration-200 cursor-pointer overflow-hidden",
                                dragActive
                                    ? "border-brand-accent bg-brand-accent/10"
                                    : "border-brand-muted/20 bg-brand-card hover:bg-brand-card/80 hover:border-brand-primary/50"
                            )}
                            onDragEnter={handleDrag}
                            onDragLeave={handleDrag}
                            onDragOver={handleDrag}
                            onDrop={handleDrop}
                        >
                            <input
                                type="file"
                                className="hidden"
                                accept="audio/*,.wav,.mp3"
                                onChange={handleChange}
                            />

                            <div className="flex flex-col items-center gap-4 text-brand-muted">
                                <div className={cn(
                                    "p-4 rounded-full transition-colors",
                                    dragActive ? "bg-brand-accent/20 text-brand-accent" : "bg-brand-primary/10 text-brand-primary"
                                )}>
                                    <UploadCloud className="w-10 h-10" />
                                </div>
                                <div className="text-center space-y-2">
                                    <p className="text-xl font-semibold text-white">
                                        Drop your audio file here
                                    </p>
                                    <p className="text-sm">
                                        or click to browse (.wav, .mp3)
                                    </p>
                                </div>
                            </div>

                            {/* Decorative background elements */}
                            <div className="absolute inset-0 pointer-events-none">
                                <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-t from-brand-background/50 to-transparent" />
                            </div>
                        </label>
                        <div className="mt-4 text-center">
                            <p className="text-xs text-brand-muted/60">Supported formats: .wav, .mp3 (Max 10MB)</p>
                            <p className="text-xs text-brand-muted/40 mt-1 flex items-center justify-center gap-1">
                                <span className="w-1.5 h-1.5 bg-brand-success/50 rounded-full"></span>
                                Audio is processed securely on-server and not stored.
                            </p>
                        </div>
                    </motion.div>
                ) : (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        key="file-selected"
                        className="w-full"
                    >
                        <div className="relative flex items-center p-6 border border-brand-accent/30 bg-brand-accent/5 rounded-2xl gap-4">
                            <div className="h-12 w-12 rounded-full bg-brand-accent/20 flex items-center justify-center text-brand-accent">
                                <FileAudio className="w-6 h-6" />
                            </div>
                            <div className="flex-1 overflow-hidden">
                                <p className="font-medium text-white truncate">{selectedFile.name}</p>
                                <p className="text-xs text-brand-muted">{(selectedFile.size / 1024 / 1024).toFixed(2)} MB</p>
                            </div>
                            <button
                                onClick={removeFile}
                                className="p-2 hover:bg-white/10 rounded-full text-brand-muted hover:text-white transition-colors"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
}
