"use client";
import {api} from "../lib/api";
import { useState } from "react";

export default function Home() {

    const [resumeId, setResumeId] =
        useState("");

    const [jobDescription, setJobDescription] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");

    const [result, setResult] =
        useState<any>(null);

    const handleSubmit = async () => {

    try {

        setLoading(true);
        setError("");
        setResult(null);

        const data = await api.matchJob(
            Number(resumeId),
            jobDescription
        );

        setResult(data);

    } catch (err: any) {

        setError(err.message);

    } finally {

        setLoading(false);

    }

};

    return (

        <main className="max-w-4xl mx-auto p-10">

            <div className="flex flex-col gap-6">

                <h1 className="text-3xl font-bold">
                    AI ATS Job Match
                </h1>

                <input
                    type="number"
                    placeholder="Resume ID"
                    className="border p-3 rounded"
                    value={resumeId}
                    onChange={(e) =>
                        setResumeId(
                            e.target.value
                        )
                    }
                />

                <textarea
                    placeholder="Paste Job Description"
                    className="border p-3 rounded h-60"
                    value={jobDescription}
                    onChange={(e) =>
                        setJobDescription(
                            e.target.value
                        )
                    }
                />

                <button
                    onClick={handleSubmit}
                    disabled={loading}
                    className="bg-black text-white p-3 rounded"
                >
                    {loading
                        ? "Analyzing..."
                        : "Analyze Match"}
                </button>

                {error && (

                    <div className="border border-red-500 p-4 rounded">

                        <p>{error}</p>

                    </div>

                )}

                {result && (

                    <div className="border p-6 rounded flex flex-col gap-6">

                        <div>

                            <h2 className="text-2xl font-bold">
                                Match Score
                            </h2>

                                <p className="text-4xl">
                                    {result.match_score}%
                                </p>

                        </div>

                        <div>

                            <h3 className="text-xl font-semibold">
                                Matched Skills
                            </h3>

                            <ul className="list-disc ml-6">

                                {result.matched_skills.map(
                                    (skill: string) => (

                                        <li key={skill}>
                                            {skill}
                                        </li>

                                    )
                                )}

                            </ul>

                        </div>

                        <div>

                            <h3 className="text-xl font-semibold">
                                Reasoning
                            </h3>

                            <ul className="list-disc ml-6">

                                {result.reasoning}

                            </ul>

                        </div>


                        <div>

                            <h3 className="text-xl font-semibold">
                                Missing Skills
                            </h3>

                            <ul className="list-disc ml-6">

                                {result.missing_skills.map(
                                    (skill: string) => (

                                        <li key={skill}>
                                            {skill}
                                        </li>

                                    )
                                )}

                            </ul>

                        </div>

                        <div>

                            <h3 className="text-xl font-semibold">
                                Recommendations
                            </h3>

                            <ul className="list-disc ml-6">

                                {result.recommendations.map(
                                    (rec: string) => (

                                        <li key={rec}>
                                            {rec}
                                        </li>

                                    )
                                )}

                            </ul>

                        </div>

                    </div>

                )}

            </div>

        </main>

    );

}