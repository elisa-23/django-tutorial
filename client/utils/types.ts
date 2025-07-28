export interface User {
  email: string;
  id: number;
  role: string | number;
  username: string;
  accessToken: string;
  refreshToken: string;
}

export interface UserForm {
  email: string;
  password: string;
  username: string;
}

export interface Question {
  question: string;
  answer: string | string[];
  incorrect: string[] | string[][];
  quizId: number;
}

export interface Quiz {
  id: number;
  title: string;
  creator: string;
  questions: Question[];
}
