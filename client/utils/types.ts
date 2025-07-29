export interface User {
    id: number
    email: string
    role: string | number
    username: string
    accessToken: string
    refreshToken: string
}

export interface UserForm {
    username: string
    email: string
    password: string
}

export interface Question {
    question: string
    answer: string | string[] | boolean | number;
    incorrect: string[] | string[][]
    type: QuestionType
    quiz?: number
}

export interface Quiz {
    id: number
    title: string
    creator: number
    types: number[]
}

export type QuestionType = "multipleChoice" | "trueOrFalse" | "dropDown" | "numerical"
