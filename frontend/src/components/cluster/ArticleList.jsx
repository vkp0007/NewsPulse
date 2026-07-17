import ArticleCard from "./ArticleCard";

function ArticleList({ articles }) {
    return (
        <section className="mt-14">

            <div className="mb-8 flex items-end justify-between">

                <div>

                    <h2 className="text-3xl font-bold tracking-tight text-black">
                        Related Articles
                    </h2>

                    <p className="mt-2 text-slate-600">
                        Explore all articles grouped within this news event.
                    </p>

                </div>

                <span className="rounded-full bg-black px-4 py-2 text-sm font-medium text-white">
                    {articles.length} Articles
                </span>

            </div>

            {articles.length === 0 ? (

                <div className="rounded-3xl border border-dashed border-slate-300 bg-white py-16 text-center">

                    <p className="text-slate-500">
                        No related articles available.
                    </p>

                </div>

            ) : (

                <div className="grid gap-6 lg:grid-cols-2">

                    {articles.map((article) => (

                        <ArticleCard
                            key={article._id}
                            article={article}
                        />

                    ))}

                </div>

            )}

        </section>
    );
}

export default ArticleList;