import { Link } from "react-router";

function ArticleCard({ article }) {

    const truncateWords = (text, limit = 22) => {
        if (!text) return "";

        const words = text.split(" ");

        return words.length > limit
            ? words.slice(0, limit).join(" ") + "..."
            : text;
    };

    return (

        <Link
            to={`/articles/${article._id}`}
            className="group block rounded-3xl border border-slate-200 bg-white p-7 transition-all duration-300 hover:-translate-y-1 hover:border-black hover:shadow-md"
        >

            <div className="flex items-center justify-between gap-4">

                <span className="rounded-full border border-red-200 bg-red-50 px-3 py-1 text-xs font-semibold text-red-700">
                    {article.source}
                </span>

                <span className="text-sm font-medium text-slate-500">
                    {new Date(article.published_at).toLocaleDateString("en-GB", {
                        day: "numeric",
                        month: "long",
                        year: "numeric",
                    })}
                </span>

            </div>

            <h3 className="mt-5 text-2xl font-semibold leading-9 tracking-tight text-black transition-colors group-hover:text-slate-800">
                {article.title}
            </h3>

            <p className="mt-4 text-[15px] leading-7 text-slate-600">
                {truncateWords(article.summary)}
            </p>

            <div className="mt-6">
                <span className="text-sm font-semibold text-black underline underline-offset-4 transition-colors group-hover:text-slate-700">
                    Read Full Article
                </span>
            </div>

        </Link>

    );
}

export default ArticleCard;