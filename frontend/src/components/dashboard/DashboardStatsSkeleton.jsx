import Skeleton from "../common/Skeleton";

function DashboardStatsSkeleton() {

    return (

        <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

            {[1, 2, 3, 4].map((item) => (

                <div
                    key={item}
                    className="rounded-2xl border border-slate-200 bg-white p-8"
                >

                    <Skeleton className="h-4 w-24" />

                    <Skeleton className="mt-6 h-10 w-16" />

                </div>

            ))}

        </section>

    );

}

export default DashboardStatsSkeleton;