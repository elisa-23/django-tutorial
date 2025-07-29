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
    answer: string|string[]
    incorrect: string[] | string[][]
    type: string
    quiz: number
    /* parts?:Array<
    | { type: "questionPart"; text: string }
    | { type: "blank"; answer: string; incorrect: string[] }
  >; */
}

export interface Quiz {
    id: number
    title: string
    creator: string
}