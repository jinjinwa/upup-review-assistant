import type { ButtonHTMLAttributes, HTMLAttributes, InputHTMLAttributes } from 'react'

export function Button(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return <button {...props} className={`button ${props.className || ''}`} />
}

export function Card(props: HTMLAttributes<HTMLDivElement>) {
  return <section {...props} className={`card ${props.className || ''}`} />
}

export function Badge(props: HTMLAttributes<HTMLSpanElement>) {
  return <span {...props} className={`badge ${props.className || ''}`} />
}

export function Input(props: InputHTMLAttributes<HTMLInputElement>) {
  return <input {...props} className={`input ${props.className || ''}`} />
}
