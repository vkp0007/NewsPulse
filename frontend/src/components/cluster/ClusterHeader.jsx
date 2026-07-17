function ClusterHeader({ cluster }) {
    return (
        <section className="border-b border-slate-200 py-5 pb-8">

            <div className="flex flex-col gap-8 lg:flex-row lg:justify-between">

                <div className="max-w-4xl">

                    <h1 className="text-5xl font-bold leading-tight tracking-tight text-black">
                        {cluster.title}
                    </h1>

                    <p className="mt-6 text-lg leading-8 text-slate-600">
                        {cluster.summary}
                    </p>

                </div>

                <div className="shrink-0 space-y-6 lg:text-right">

                    <div>

                        <p className="text-sm font-medium text-slate-500">
                            First Detected
                        </p>

                        <p className="mt-1 font-semibold text-slate-900">
                            {new Date(cluster.start_time).toLocaleDateString("en-GB", {
                                day: "numeric",
                                month: "long",
                                year: "numeric",
                            })}
                        </p>

                    </div>

                    <div>

                        <p className="text-sm font-medium text-slate-500">
                            Last Updated
                        </p>

                        <p className="mt-1 font-semibold text-slate-900">
                            {new Date(cluster.updated_at).toLocaleDateString("en-GB", {
                                day: "numeric",
                                month: "long",
                                year: "numeric",
                            })}
                        </p>

                    </div>

                </div>

            </div>

        </section>
    );
}

export default ClusterHeader;