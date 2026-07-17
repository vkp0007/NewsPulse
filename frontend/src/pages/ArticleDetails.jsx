import { useEffect, useState } from "react";
import { useParams } from "react-router";

import { getArticleById } from "../services/articleApi";

function ArticleDetails() {
    const { id } = useParams();

    const [article, setArticle] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchArticle = async () => {
            try {
                const data = await getArticleById(id);
                setArticle(data);
            } catch (err) {
                console.error(err);
                setError("Failed to load article.");
            } finally {
                setLoading(false);
            }
        };

        fetchArticle();
    }, [id]);

    if (loading) {
        return (
            <div className="py-24 text-center text-slate-500">
                Loading article...
            </div>
        );
    }

    if (error) {
        return (
            <div className="py-24 text-center text-red-500">
                {error}
            </div>
        );
    }

    if (!article) {
        return (
            <div className="py-24 text-center text-slate-500">
                Article not found.
            </div>
        );
    }

    return (
        <article className="mx-auto max-w-5xl py-6">

            <section className="border-b border-slate-200 pb-10">

                <div className="flex flex-col gap-10 lg:flex-row lg:justify-between">

                    <div className="max-w-4xl">

                        <h1 className="text-5xl font-bold leading-tight tracking-tight text-black">
                            {article.title}
                        </h1>

                        <p className="mt-6 text-lg leading-8 text-slate-600">
                            {article.summary}
                        </p>

                        <a
                            href={article.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="mt-8 inline-flex rounded-xl bg-black px-6 py-3 font-medium text-white transition-all duration-300 hover:bg-slate-800"
                        >
                            Read Original Article
                        </a>

                    </div>

                    <div className="shrink-0 space-y-6 lg:min-w-55 lg:text-right">

                        <div>

                            <p className="text-sm font-medium text-slate-500">
                                Source
                            </p>

                            <span className="mt-2 inline-block rounded-full border border-red-200 bg-red-50 px-3 py-1 text-xs font-semibold text-red-700">
                                {article.source}
                            </span>

                        </div>

                        <div>

                            <p className="text-sm font-medium text-slate-500">
                                Published
                            </p>

                            <p className="mt-1 font-semibold text-slate-900">
                                {new Date(article.published_at).toLocaleDateString(
                                    "en-GB",
                                    {
                                        day: "numeric",
                                        month: "long",
                                        year: "numeric",
                                    }
                                )}
                            </p>

                        </div>

                        {article.author && (
                            <div>

                                <p className="text-sm font-medium text-slate-500">
                                    Author
                                </p>

                                <p className="mt-1 font-semibold text-slate-900">
                                    {article.author}
                                </p>

                            </div>
                        )}

                    </div>

                </div>

            </section>

            {article.image_url && (
                <img
                    src={article.image_url}
                    alt={article.title}
                    className="mt-10 w-full rounded-2xl border border-slate-200 object-cover shadow-sm"
                />
            )}

            <section className="mt-12 border-t border-slate-200 pt-10">

                <h2 className="mb-6 text-2xl font-bold tracking-tight text-black">
                    Full Article
                </h2>

                <div className="prose prose-slate max-w-none">

                    <p className="whitespace-pre-line text-[17px] leading-8 text-slate-700">
                        {article.content}
                    </p>

                </div>

            </section>

        </article>
    );
}

export default ArticleDetails;