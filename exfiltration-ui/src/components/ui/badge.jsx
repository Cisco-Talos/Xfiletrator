export function Badge({ children, variant = "default" }) {
const baseStyles = "inline-flex items-center px-2.5 py-0.5 rounded text-xs font-medium";
const variants = {
default: "bg-blue-100 text-blue-800",
secondary: "bg-gray-100 text-gray-800",
danger: "bg-red-100 text-red-800",
};
return <span className={`${baseStyles} ${variants[variant]}`}>{children}</span>;
}
