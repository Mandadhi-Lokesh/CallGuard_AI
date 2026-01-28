import { forwardRef } from 'react';
import { cn } from '../lib/utils';
import { motion } from 'framer-motion';

const Button = forwardRef(({ className, variant = 'primary', size = 'default', children, ...props }, ref) => {
    const variants = {
        primary: 'bg-brand-primary text-white hover:bg-brand-primary/90 shadow-[0_0_15px_rgba(59,130,246,0.5)] border-brand-accent/20 border',
        secondary: 'bg-brand-card text-brand-text border border-brand-muted/20 hover:bg-brand-muted/10',
        outline: 'bg-transparent border border-brand-primary text-brand-primary hover:bg-brand-primary/10',
        ghost: 'bg-transparent text-brand-text hover:bg-brand-muted/10',
    };

    const sizes = {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 px-3',
        lg: 'h-12 px-8 text-lg',
        icon: 'h-10 w-10',
    };

    return (
        <motion.button
            ref={ref}
            whileTap={{ scale: 0.98 }}
            className={cn(
                'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-primary disabled:pointer-events-none disabled:opacity-50 select-none',
                variants[variant],
                sizes[size],
                className
            )}
            {...props}
        >
            {children}
        </motion.button>
    );
});

Button.displayName = 'Button';

export { Button };
