export function Input({ className = "", ...props }) {
return (
<input
className={`w-full rounded-md border border-gray-300 bg-white dark:bg-zinc-900 text-black dark:text-white p-2 text-sm placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 ${className}`}
{...props}
/>
);
}
