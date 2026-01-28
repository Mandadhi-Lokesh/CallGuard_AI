import { Header } from './Header';

export function Layout({ children }) {
    return (
        <div className="min-h-screen flex flex-col bg-brand-background text-brand-text">
            <Header />
            <main className="flex-1">
                {children}
            </main>
            <footer className="border-t border-white/5 py-8 mt-auto">
                <div className="container mx-auto px-4 text-center text-brand-muted text-sm">
                    <p>© 2026 CallGuard AI. Protecting India from fraud.</p>
                </div>
            </footer>
        </div>
    );
}
