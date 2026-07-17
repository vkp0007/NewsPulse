function Badge({
    children,
}) {
    return (
        <span className="rounded-full bg-slate-100 px-3 py-1 text-sm font-medium text-slate-700">
            {children}
        </span>
    );
}

export default Badge;