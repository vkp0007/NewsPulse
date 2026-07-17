function StatCard({
    title,
    value,
}) {
    return (
        <div className="rounded-xl border border-slate-200 bg-white p-6 py-10 shadow-sm">

            <p className="text-sm text-slate-500">
                {title}
            </p>

            <h2 className="mt-2 text-3xl font-bold text-slate-900">
                {value}
            </h2>

        </div>
    );
}

export default StatCard;