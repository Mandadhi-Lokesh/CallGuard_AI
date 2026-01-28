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
                    <p>© 2026 CallGuard AI. Protecting India.</p>

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
            </footer>
        </div>
    );
}
