import { Link, useLocation } from 'react-router-dom';
import { cn } from '../lib/utils';
import { ShieldCheck } from 'lucide-react';
import { motion } from 'framer-motion';

export function Header() {
    const location = useLocation();

    const navItems = [
        { name: 'Home', path: '/' },
        { name: 'Analyzer', path: '/analyzer' },
        { name: 'Impact', path: '/impact' },
        { name: 'About', path: '/about' },
    ];

    return (
        <header className="sticky top-0 z-50 w-full border-b border-white/5 bg-brand-background/80 backdrop-blur-md supports-[backdrop-filter]:bg-brand-background/60">
            <div className="container mx-auto flex h-16 items-center justify-between px-4">
                <Link to="/" className="flex items-center gap-2 group">
                    <div className="relative flex items-center justify-center w-8 h-8 rounded-lg bg-brand-primary/20 group-hover:bg-brand-primary/30 transition-colors">
                        <ShieldCheck className="w-5 h-5 text-brand-accent" />
                    </div>
                    <span className="font-bold text-xl tracking-tight text-white group-hover:text-brand-accent transition-colors">
                        CallGuard AI
                    </span>
                </Link>
                <nav className="hidden md:flex gap-6">
                    {navItems.map((item) => (
                        <Link
                            key={item.path}
                            to={item.path}
                            className={cn(
                                "relative text-sm font-medium transition-colors hover:text-brand-accent",
                                location.pathname === item.path ? "text-brand-accent" : "text-brand-muted"
                            )}
                        >
                            {item.name}
                            {location.pathname === item.path && (
                                <motion.div
                                    layoutId="navbar-indicator"
                                    className="absolute -bottom-[21px] left-0 right-0 h-[2px] bg-brand-accent shadow-[0_0_10px_rgba(59,130,246,0.8)]"
                                    initial={false}
                                    transition={{ type: "spring", stiffness: 380, damping: 30 }}
                                />
                            )}
                        </Link>
                    ))}
                </nav>
                <div className="flex md:hidden">
                    {/* Mobile menu could go here, keeping it detailed but minimal for desktop focus first */}
                </div>
            </div>
        </header>
    );
}
