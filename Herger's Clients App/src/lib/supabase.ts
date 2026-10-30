import { createClient, type Session, type User } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL ?? ''
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY ?? ''

export const supabase = supabaseUrl && supabaseAnonKey
  ? createClient(supabaseUrl, supabaseAnonKey, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
      },
    })
  : null

export type AuthResult = {
  data: { user: User | null; session: Session | null } | null
  error: Error | null
}

function missingSupabaseConfigError() {
  return new Error(
    'Supabase is not configured yet. Add VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY to your environment before signing in.',
  )
}

export async function signInWithEmailPassword({
  email,
  password,
}: {
  email: string
  password: string
}): Promise<AuthResult> {
  if (!supabase) {
    return { data: null, error: missingSupabaseConfigError() }
  }

  const { data, error } = await supabase.auth.signInWithPassword({ email, password })

  return {
    data,
    error: error ? new Error(error.message) : null,
  }
}

export async function signUpWithEmailPassword({
  email,
  password,
  fullName,
}: {
  email: string
  password: string
  fullName: string
}): Promise<AuthResult> {
  if (!supabase) {
    return { data: null, error: missingSupabaseConfigError() }
  }

  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: {
        full_name: fullName,
      },
    },
  })

  return {
    data,
    error: error ? new Error(error.message) : null,
  }
}
