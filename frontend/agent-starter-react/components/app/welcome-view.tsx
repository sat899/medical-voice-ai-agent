import { Button } from '@/components/ui/button';

function DawnLogo({ className }: { className?: string }) {
  return (
    <div className={className}>
      <svg
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="text-dawn-accent"
      >
        {/* Sunrise arc */}
        <circle cx="24" cy="32" r="12" stroke="currentColor" strokeWidth="2" fill="none" opacity="0.3" />
        <circle cx="24" cy="32" r="8" stroke="currentColor" strokeWidth="2" fill="none" opacity="0.5" />
        <circle cx="24" cy="32" r="4" fill="currentColor" opacity="0.8" />
        {/* Rays */}
        <line x1="24" y1="6" x2="24" y2="14" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        <line x1="8" y1="20" x2="14" y2="24" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        <line x1="40" y1="20" x2="34" y2="24" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        <line x1="12" y1="10" x2="17" y2="16" stroke="currentColor" strokeWidth="2" strokeLinecap="round" opacity="0.6" />
        <line x1="36" y1="10" x2="31" y2="16" stroke="currentColor" strokeWidth="2" strokeLinecap="round" opacity="0.6" />
      </svg>
    </div>
  );
}

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = ({
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeViewProps) => {
  return (
    <div ref={ref} className="flex h-svh w-svw items-center justify-center">
      {/* Split layout even on welcome */}
      <div className="flex h-full w-full flex-col md:flex-row">
        {/* Left — Dawn branding panel */}
        <div className="dawn-panel flex w-full flex-col items-center justify-center gap-6 border-b border-border/40 md:w-1/3 md:border-r md:border-b-0">
          <DawnLogo className="mb-2" />
          <h1 className="text-dawn-accent font-mono text-3xl font-bold tracking-widest uppercase">
            Dawn
          </h1>
          <p className="text-muted-foreground max-w-[220px] text-center text-sm leading-relaxed">
            Medical voice assistant — powered by AI
          </p>
          <Button
            size="lg"
            onClick={onStartCall}
            className="dawn-button mt-4 w-56 rounded-full font-mono text-xs font-bold tracking-wider uppercase"
          >
            {startButtonText}
          </Button>
        </div>

        {/* Right — placeholder transcript area */}
        <div className="flex flex-1 flex-col items-center justify-center gap-4 p-8">
          <div className="flex flex-col items-center gap-3 opacity-40">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" className="text-muted-foreground">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <p className="text-muted-foreground text-center text-sm">
              Conversation transcript will appear here
            </p>
            <p className="text-muted-foreground/60 text-center text-xs">
              Start a call to begin
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
