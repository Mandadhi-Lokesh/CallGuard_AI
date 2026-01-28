import { cn } from '../lib/utils';

export function Card({ className, children, ...props }) {
    return (
        <div
            className={cn(
                "rounded-xl border border-white/5 bg-brand-card p-6 shadow-xl backdrop-blur-sm",
                className
            )}
            {...props}
        >
            {children}
        </div>
    );
}
