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

interface BaseQuestion {  //dont export, DONT NAME AS JUST QUESTION
    question: string
    quiz?: number
}

export interface Quiz {
    id: number
    title: string
    creator: number
    types: number[] | string[]
}

export type QuestionType = "multiple_choice" | "true/false" | "dropdown" | "numerical"

export interface CreateMultipleChoiceQuestion extends BaseQuestion {
    type: "multiple_choice"
    answer: string
    incorrect: string[]
}

export interface CreateTrueOrFalseQuestion extends BaseQuestion {
    type: "true/false"
    answer: boolean
}

export interface CreateNumericalQuestion extends BaseQuestion {
    type: "numerical"
    answer: number
}

export interface CreateDropDownQuestion extends BaseQuestion {
    type: "dropdown"
    answer: string[]
    incorrect: string[][]
}

export type CreateQuestion = CreateMultipleChoiceQuestion | CreateTrueOrFalseQuestion | CreateNumericalQuestion | CreateDropDownQuestion