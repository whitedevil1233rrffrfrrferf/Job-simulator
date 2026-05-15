const BASE_URL =
    process.env.NEXT_PUBLIC_API_BASE_URL;

const getHeaders = () => {

    return {
        "Content-Type": "application/json",
    };

};

export const api = {

    matchJob: async (
        resume_id: number,
        job_description: string
    ) => {

        const res = await fetch(
            `${BASE_URL}/match/`,
            {
                method: "POST",

                headers: getHeaders(),

                body: JSON.stringify({
                    resume_id,
                    job_description,
                }),
            }
        );

        if (!res.ok) {
            throw new Error(
                "Failed to analyze ATS match"
            );
        }

        return res.json();

    },
    generateResumeImprovements: async (
        resume_id: number,
        job_description: string
    ) => {

        const res = await fetch(
            `${BASE_URL}/resume-improvement/generate`,
            {
                method: "POST",

                headers: getHeaders(),

                body: JSON.stringify({
                    resume_id,
                    job_description,
                }),
            }
        );

        if (!res.ok) {

            throw new Error(
                "Failed to generate resume improvements"
            );

        }

        return res.json();

    },
    generateCoverLetter: async (
        resume_id: number,
        job_description: string
    ) => {

        const res = await fetch(
        `${BASE_URL}/cover-letter/generate`,
        {
            method: "POST",

            headers: getHeaders(),

            body: JSON.stringify({
            resume_id,
            job_description,
            }),
        }
        );

        if (!res.ok) {
        throw new Error(
            "Failed to generate cover letter"
        );
        }

        return res.json();
    },

};