import { Header } from './Header';

export function Layout({ children }) {
    return (
        <div className="min-h-screen flex flex-col bg-brand-background text-brand-text">
            <Header />
            <main className="flex-1">
                {children}
            </main>
            <footer className="border-t border-white/5 py-8 mt-auto bg-black/20">
                <div className="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-brand-muted">
                    <div className="flex flex-col md:flex-row gap-2 md:gap-8 items-center">
                        <p>© 2026 CallGuard AI</p>
                        <p className="text-white/40 hidden md:block">|</p>
                        <p>India AI Impact Buildathon</p>
                        <p className="text-white/40 hidden md:block">|</p>
                        <p>Team: CyberSentinels</p>
                    </div>

                    <div className="flex items-center gap-6">
                        <div className="flex items-center gap-2">
                            <span className="relative flex h-2 w-2">
                                <span className="relative inline-flex rounded-full h-2 w-2 bg-brand-success"></span>
                            </span>
                            <span className="font-mono text-xs text-brand-success/90">SYSTEM OPERATIONAL</span>
                        </div>
                        <div className="font-mono text-xs opacity-50">
                            v2.1.0-alpha
                        </div>
                    </div>
                </div>

                <div className="mt-8 pt-4 border-t border-white/5 text-center px-4">
                    <p className="text-xs text-brand-muted/40">
                        Disclaimer: This project is a functional prototype built for the India AI Impact Buildathon. The system demonstrates the feasibility of AI-assisted call fraud detection using heuristic and pattern-based inference.
                    </p>
                </div>
            </footer>
        </div>
    );
}
