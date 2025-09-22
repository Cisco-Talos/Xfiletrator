// File: exfiltration-ui/src/components/ui/card.jsx

import React from "react";

export function Card({ children, className = "", ...props }) {
  return (
    <div
      className={`bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-700 rounded-lg shadow ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}

export function CardContent({ children, className = "", ...props }) {
  return (
    <div className={`p-4 ${className}`} {...props}>
      {children}
    </div>
  );
}
