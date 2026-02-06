'use client';

import React, { useEffect, useRef } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { useSessionContext, useSessionMessages, useVoiceAssistant } from '@livekit/components-react';
import type { AppConfig } from '@/app-config';
import { AgentAudioVisualizerBar } from '@/components/agents-ui/agent-audio-visualizer-bar';
import { AgentDisconnectButton } from '@/components/agents-ui/agent-disconnect-button';
import { AgentTrackToggle } from '@/components/agents-ui/agent-track-toggle';
import { Shimmer } from '../ai-elements/shimmer';

const MotionDiv = motion.create('div');

const FADE_IN = {
  variants: {
    visible: { opacity: 1 },
    hidden: { opacity: 0 },
  },
  initial: 'hidden',
  animate: 'visible',
  exit: 'hidden',
  transition: { duration: 0.4, ease: 'easeOut' },
};

interface SessionViewProps {
  appConfig: AppConfig;
}

export const SessionView = ({
  appConfig,
  ...props
}: React.ComponentProps<'section'> & SessionViewProps) => {
  const session = useSessionContext();
  const { messages } = useSessionMessages(session);
  const { state: agentState, audioTrack: agentAudioTrack } = useVoiceAssistant();
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll transcript to bottom on new messages
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <section className="relative z-10 flex h-svh w-svw flex-col overflow-hidden md:flex-row" {...props}>
      {/* ──────────────── LEFT PANEL: Dawn Voice ──────────────── */}
      <div className="dawn-panel relative flex w-full shrink-0 flex-col items-center justify-between border-b border-border/30 md:w-1/3 md:border-r md:border-b-0">
        {/* Top: brand */}
        <div className="flex flex-col items-center pt-10">
          <h1 className="text-dawn-accent font-mono text-2xl font-bold tracking-widest uppercase">
            Dawn
          </h1>
          <p className="text-muted-foreground mt-1 text-xs tracking-wide">
            Medical Voice Assistant
          </p>
        </div>

        {/* Center: visualizer */}
        <div className="flex flex-1 flex-col items-center justify-center gap-4">
          <div className="dawn-visualizer-ring relative flex items-center justify-center rounded-full p-8">
            <AgentAudioVisualizerBar
              state={agentState}
              audioTrack={agentAudioTrack}
              barCount={7}
              size="lg"
              className="text-dawn-accent"
            />
          </div>

          {/* Agent state label */}
          <AnimatePresence mode="wait">
            <MotionDiv
              key={agentState}
              {...FADE_IN}
              className="font-mono text-xs tracking-wider uppercase"
            >
              {agentState === 'listening' && (
                <span className="text-dawn-accent">Listening…</span>
              )}
              {agentState === 'thinking' && (
                <span className="text-muted-foreground animate-pulse">Thinking…</span>
              )}
              {agentState === 'speaking' && (
                <span className="text-dawn-accent">Speaking…</span>
              )}
              {agentState === 'connecting' && (
                <span className="text-muted-foreground animate-pulse">Connecting…</span>
              )}
              {agentState === 'initializing' && (
                <span className="text-muted-foreground animate-pulse">Initialising…</span>
              )}
            </MotionDiv>
          </AnimatePresence>

          {/* Pre-connect shimmer hint */}
          {appConfig.isPreConnectBufferEnabled && messages.length === 0 && (
            <Shimmer
              duration={2}
              className="text-muted-foreground pointer-events-none px-6 text-center text-sm font-medium"
            >
              Listening — ask a question to begin
            </Shimmer>
          )}
        </div>

        {/* Bottom: controls */}
        <div className="flex flex-row items-center gap-3 pb-8">
          <AgentTrackToggle
            source="microphone"
            className="dawn-control-btn rounded-full"
          />
          <AgentDisconnectButton
            size="default"
            className="rounded-full"
          />
        </div>
      </div>

      {/* ──────────────── RIGHT PANEL: Transcript ──────────────── */}
      <div className="relative flex min-h-0 flex-1 flex-col">
        {/* Header */}
        <div className="flex shrink-0 items-center justify-between border-b border-border/30 px-6 py-4">
          <div className="flex items-center gap-2">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" className="text-dawn-accent">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <span className="font-mono text-xs font-semibold tracking-wider uppercase text-foreground">
              Conversation
            </span>
          </div>
          <span className="font-mono text-xs text-muted-foreground">
            {messages.length} message{messages.length !== 1 ? 's' : ''}
          </span>
        </div>

        {/* Transcript body */}
        <div ref={scrollRef} className="flex-1 overflow-y-auto">
          {messages.length === 0 ? (
            <div className="flex h-full flex-col items-center justify-center gap-3 opacity-30">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" className="text-muted-foreground">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="currentColor" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
              <p className="text-muted-foreground text-sm">
                Waiting for conversation…
              </p>
            </div>
          ) : (
            <div className="dawn-transcript space-y-1 px-4 py-4 md:px-6">
              {messages.map((receivedMessage) => {
                const { id, timestamp, from, message } = receivedMessage;
                const isUser = from?.isLocal === true;
                const time = new Date(timestamp);
                const timeStr = time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

                return (
                  <MotionDiv
                    key={id}
                    initial={{ opacity: 0, y: 8 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.25, ease: 'easeOut' }}
                    className={`flex flex-col gap-1 rounded-xl px-4 py-3 ${
                      isUser
                        ? 'ml-8 bg-dawn-accent/10 self-end'
                        : 'mr-8 bg-secondary self-start'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <span className={`font-mono text-[10px] font-bold uppercase tracking-wider ${
                        isUser ? 'text-dawn-accent' : 'text-foreground/70'
                      }`}>
                        {isUser ? 'You' : 'Dawn'}
                      </span>
                      <span className="text-muted-foreground text-[10px]">{timeStr}</span>
                    </div>
                    <p className="text-foreground text-sm leading-relaxed">{message}</p>
                  </MotionDiv>
                );
              })}

              {/* Thinking indicator */}
              {agentState === 'thinking' && (
                <div className="mr-8 flex items-center gap-2 rounded-xl bg-secondary px-4 py-3">
                  <div className="flex gap-1">
                    <span className="bg-dawn-accent/60 inline-block h-1.5 w-1.5 animate-bounce rounded-full [animation-delay:0ms]" />
                    <span className="bg-dawn-accent/60 inline-block h-1.5 w-1.5 animate-bounce rounded-full [animation-delay:150ms]" />
                    <span className="bg-dawn-accent/60 inline-block h-1.5 w-1.5 animate-bounce rounded-full [animation-delay:300ms]" />
                  </div>
                  <span className="text-muted-foreground text-xs">Dawn is thinking…</span>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </section>
  );
};
