import Badge from "./Badge";

function SourceList({
    sources,
}) {
    return (
        <section>

            <h2 className="mb-4 text-xl font-semibold">
                Sources
            </h2>

            <div className="flex flex-wrap gap-3">

                {sources.map((source) => (
                    <Badge key={source}>
                        {source}
                    </Badge>
                ))}

            </div>

        </section>
    );
}

export default SourceList;