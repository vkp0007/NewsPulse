function SearchBar({
    query,
    setQuery,
    onSearch,
}) {

    const handleKeyDown = (e) => {

        if (e.key === "Enter") {
            onSearch();
        }

    };

    return (

        <div className="flex gap-4">

            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Search by title, topic or source..."
                className="flex-1 rounded-2xl border border-slate-300 px-5 py-4 outline-none transition focus:border-black"
            />

            <button
                onClick={onSearch}
                className="rounded-2xl bg-black px-8 font-medium text-white transition hover:bg-slate-800"
            >
                Search
            </button>

        </div>

    );
}

export default SearchBar;