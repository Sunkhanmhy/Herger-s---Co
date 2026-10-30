import { useEffect, useMemo, useState, type ReactNode } from 'react'
import { Navigate, NavLink, Route, Routes, useLocation, useNavigate } from 'react-router-dom'
import { signInWithEmailPassword, signUpWithEmailPassword, supabase } from './lib/supabase'

type NavItem = {
  label: string
  path: string
  icon: string
  description?: string
}

type NewsItem = {
  id: number
  title: string
  category: 'News' | 'Event'
  date: string
  time: string
  summary: string
  image: string
}

const logoUrl = '/images/hergers-logo.png'

const navItems: NavItem[] = [
  { label: 'Dashboard', path: '/dashboard', icon: '⌂' },
  { label: 'News & Events', path: '/news-events', icon: '▣' },
  { label: 'Bookings & Sessions', path: '/bookings', icon: '🗓' },
  { label: 'Recent Bookings', path: '/recent-bookings', icon: '⏱' },
  { label: 'Profile Settings', path: '/profile', icon: '◔' },
  { label: 'Payment Checkout', path: '/payments', icon: '◫' },
  { label: 'IT Support', path: '/support', icon: '◌' },
  { label: 'Documents', path: '/documents', icon: '▤' },
]

const newsItems: NewsItem[] = [
  {
    id: 1,
    title: 'New Corporate Governance Guidelines Released',
    category: 'News',
    date: 'Apr 28, 2025',
    time: '10:24 AM',
    summary:
      'The Federal Government has released new corporate governance guidelines aimed at strengthening transparency and accountability in the business sector.',
    image: '/images/courtroom-01.jpg',
  },
  {
    id: 2,
    title: 'Join Our Webinar: Understanding Intellectual Property Rights',
    category: 'Event',
    date: 'Apr 25, 2025',
    time: '2:30 PM',
    summary:
      'We invite you to our upcoming webinar on intellectual property rights, where our senior partners will discuss key legal considerations for businesses and creators.',
    image: '/images/courtroom-02.jpg',
  },
  {
    id: 3,
    title: 'Landmark Ruling on Employment Rights Sets New Precedent',
    category: 'News',
    date: 'Apr 22, 2025',
    time: '11:15 AM',
    summary:
      'A recent high court ruling has set a new precedent on employee rights, offering stronger protections for workers in the private sector.',
    image: '/images/courtroom-03.jpg',
  },
  {
    id: 4,
    title: 'Annual Legal Conference 2025 — Save the Date',
    category: 'Event',
    date: 'Apr 18, 2025',
    time: '4:20 PM',
    summary:
      'Our annual legal conference will be held on July 15–17, 2025, at the Lagos Continental Hotel. This year’s theme is “The Future of Law in a Digital World.”',
    image: '/images/courtroom-04.jpg',
  },
  {
    id: 5,
    title: 'Updated Client Privacy Policy',
    category: 'News',
    date: 'Apr 15, 2025',
    time: '9:45 AM',
    summary:
      'We have updated our privacy policy to better protect your data and ensure compliance with the latest data protection regulations.',
    image: '/images/office-01.jpg',
  },
  {
    id: 6,
    title: 'Pro Bono Legal Clinics This Quarter',
    category: 'Event',
    date: 'Apr 12, 2025',
    time: '1:00 PM',
    summary:
      'We are pleased to announce our pro bono legal clinics, offering free legal consultations to eligible individuals and small businesses in our community.',
    image: '/images/office-02.jpg',
  },
  {
    id: 7,
    title: 'Cybersecurity and Data Protection: What Businesses Need to Know',
    category: 'News',
    date: 'Apr 10, 2025',
    time: '8:30 AM',
    summary:
      'Our latest article explores essential cybersecurity practices and how to protect your business from emerging digital threats.',
    image: '/images/office-03.jpg',
  },
  {
    id: 8,
    title: 'Webinar: Navigating Tax Law Changes in 2025',
    category: 'Event',
    date: 'Apr 8, 2025',
    time: '3:00 PM',
    summary:
      'Join us for a live webinar on the latest tax law changes and what they mean for individuals and businesses. Expert insights, practical tips and Q&A included.',
    image: '/images/mining-01.jpg',
  },
]

const featureList = [
  {
    title: 'Expert Legal Guidance',
    text: 'Get trusted advice from experienced legal professionals.',
    icon: '⚖',
  },
  {
    title: 'Book Sessions',
    text: 'Schedule consultations and legal sessions with ease.',
    icon: '📅',
  },
  {
    title: 'Latest News & Insights',
    text: 'Stay informed with the latest legal updates and resources.',
    icon: '📰',
  },
]

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignUpPage />} />
      <Route path="/dashboard" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/news-events" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/bookings" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/recent-bookings" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/profile" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/payments" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/support" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="/documents" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  )
}

function ProtectedRoute({ children }: { children: ReactNode }) {
  const [isReady, setIsReady] = useState(false)
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  useEffect(() => {
    let isMounted = true

    const syncSession = async () => {
      if (!supabase) {
        setIsAuthenticated(false)
        setIsReady(true)
        return
      }

      try {
        const {
          data: { session },
        } = await supabase.auth.getSession()

        if (isMounted) {
          setIsAuthenticated(Boolean(session))
        }
      } catch {
        if (isMounted) {
          setIsAuthenticated(false)
        }
      } finally {
        if (isMounted) {
          setIsReady(true)
        }
      }
    }

    syncSession()

    const subscription = supabase
      ? supabase.auth.onAuthStateChange((_event, session) => {
          if (isMounted) {
            setIsAuthenticated(Boolean(session))
            setIsReady(true)
          }
        }).data.subscription
      : null

    return () => {
      isMounted = false
      subscription?.unsubscribe()
    }
  }, [])

  if (!isReady) {
    return <div className="auth-loading">Loading your secure workspace…</div>
  }

  return isAuthenticated ? <>{children}</> : <Navigate to="/login" replace />
}

function LoginPage() {
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  useEffect(() => {
    setError('')
  }, [])

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError('')

    if (!email || !password) {
      setError('Please provide both email and password.')
      return
    }

    setIsSubmitting(true)

    try {
      const { data, error: signInError } = await signInWithEmailPassword({ email, password })

      if (signInError || !data?.user) {
        throw new Error(signInError?.message ?? 'Unable to sign in today.')
      }

      navigate('/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed. Please try again.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <AuthShell
      leftTitle="Herger's & Co."
      subTitle="Justice • Integrity • Results"
      badge="Welcome to"
      formTitle="Sign In to Your Account"
      description="Access your dashboard, book sessions, read the latest legal news and more."
      form={
        <form onSubmit={handleSubmit} className="auth-form">
          <label className="field">
            <span className="field-icon">✉</span>
            <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="Email address" aria-label="Email address" />
          </label>

          <label className="field">
            <span className="field-icon">◒</span>
            <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} placeholder="Password" aria-label="Password" />
          </label>

          {error ? <div className="error-box">{error}</div> : null}

          <div className="auth-row">
            <label className="checkbox-row">
              <input type="checkbox" defaultChecked />
              <span>Remember me</span>
            </label>
            <button type="button" className="text-link">Forgot password?</button>
          </div>

          <button type="submit" className="primary-button" disabled={isSubmitting}>
            {isSubmitting ? 'Signing In…' : 'Sign In'}
            <span>→</span>
          </button>

          <div className="divider"><span>or</span></div>

          <button type="button" className="social-button google-button"><span className="social-mark">G</span>Continue with Google</button>
          <button type="button" className="social-button microsoft-button"><span className="social-mark">▣</span>Continue with Microsoft</button>

          <p className="switch-line">
            Don’t have an account? <button type="button" className="text-link" onClick={() => navigate('/signup')}>Sign Up</button>
          </p>
        </form>
      }
    />
  )
}

function SignUpPage() {
  const navigate = useNavigate()
  const [form, setForm] = useState({ fullName: '', email: '', password: '' })
  const [error, setError] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError('')

    if (!form.fullName || !form.email || !form.password) {
      setError('Please complete all fields to create your account.')
      return
    }

    if (form.password.length < 8) {
      setError('Password must be at least 8 characters long.')
      return
    }

    setIsSubmitting(true)

    try {
      const { data, error: signUpError } = await signUpWithEmailPassword({
        email: form.email,
        password: form.password,
        fullName: form.fullName,
      })

      if (signUpError || !data?.user) {
        throw new Error(signUpError?.message ?? 'Unable to create your account right now.')
      }

      navigate('/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Signup failed. Please try again.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <AuthShell
      leftTitle="Herger's & Co."
      subTitle="Justice • Integrity • Results"
      badge="Create your"
      formTitle="Sign Up for Client Access"
      description="Build your secure client profile, manage legal sessions and receive the latest updates from our team."
      form={
        <form onSubmit={handleSubmit} className="auth-form">
          <label className="field">
            <span className="field-icon">◉</span>
            <input type="text" name="fullName" value={form.fullName} onChange={handleChange} placeholder="Full name" aria-label="Full name" />
          </label>

          <label className="field">
            <span className="field-icon">✉</span>
            <input type="email" name="email" value={form.email} onChange={handleChange} placeholder="Email address" aria-label="Email address" />
          </label>

          <label className="field">
            <span className="field-icon">◒</span>
            <input type="password" name="password" value={form.password} onChange={handleChange} placeholder="Password" aria-label="Password" />
          </label>

          {error ? <div className="error-box">{error}</div> : null}

          <button type="submit" className="primary-button" disabled={isSubmitting}>
            {isSubmitting ? 'Creating account…' : 'Create account'}
            <span>→</span>
          </button>

          <p className="switch-line">
            Already have an account? <button type="button" className="text-link" onClick={() => navigate('/login')}>Sign In</button>
          </p>
        </form>
      }
    />
  )
}

function DashboardLayout() {
  const location = useLocation()
  const navigate = useNavigate()
  const currentItem = useMemo(
    () => navItems.find((item) => item.path === location.pathname) ?? navItems[0],
    [location.pathname],
  )

  const handleSignOut = async () => {
    if (supabase) {
      await supabase.auth.signOut()
    }
    navigate('/login')
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand-row">
          <img src={logoUrl} alt="Herger's & Co. logo" className="brand-mark" />
          <div>
            <div className="brand-name">Herger's & Co.</div>
            <div className="brand-subtitle">Justice • Integrity • Results</div>
          </div>
        </div>

        <nav className="sidebar-nav">
          {navItems.map((item) => (
            <NavLink key={item.path} to={item.path} className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <span className="nav-icon">{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>

        <button type="button" className="signout-button" onClick={handleSignOut}>← Sign Out</button>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div className="search-box">
            <span className="search-icon">⌕</span>
            <input type="text" defaultValue="Search news, events or topics..." aria-label="Search" />
          </div>
          <div className="topbar-right">
            <button type="button" className="notification-button" aria-label="Notifications">
              🔔
              <span className="notification-badge">3</span>
            </button>
            <div className="profile-chip">
              <img src="/images/portrait-03.jpg" alt="Daniel Johnson" />
              <div>
                <strong>Good morning,</strong>
                <span>Daniel Johnson</span>
              </div>
            </div>
          </div>
        </header>

        <div className="content-area">
          <div className="route-header">
            <div className="route-title-wrap">
              <span className="route-icon">{currentItem.icon}</span>
              <div>
                <h1>{currentItem.label}</h1>
                <p>{currentItem.description ?? 'Stay connected with your legal support and case updates.'}</p>
              </div>
            </div>
          </div>
          <PageRenderer />
        </div>

        <nav className="mobile-bottom-nav" aria-label="Main navigation">
          {navItems.slice(0, 4).map((item) => (
            <NavLink key={item.path} to={item.path} className={({ isActive }) => `bottom-nav-item ${isActive ? 'active' : ''}`}>
              <span>{item.icon}</span>
              <small>{item.label}</small>
            </NavLink>
          ))}
        </nav>
      </main>
    </div>
  )
}

function PageRenderer() {
  const location = useLocation()

  switch (location.pathname) {
    case '/dashboard':
      return <DashboardHome />
    case '/news-events':
      return <NewsEventsPage />
    case '/bookings':
      return <BookingsPage />
    case '/recent-bookings':
      return <RecentBookingsPage />
    case '/profile':
      return <ProfilePage />
    case '/payments':
      return <PaymentsPage />
    case '/support':
      return <SupportPage />
    case '/documents':
      return <DocumentsPage />
    default:
      return <DashboardHome />
  }
}

function DashboardHome() {
  const stats = [
    { label: 'Open matters', value: '12', detail: '4 require review' },
    { label: 'Upcoming sessions', value: '03', detail: '2 confirmed' },
    { label: 'Documents', value: '18', detail: '5 signed' },
  ]

  return (
    <section className="dashboard-grid">
      <div className="stats-row">
        {stats.map((stat) => (
          <article key={stat.label} className="stat-card">
            <span>{stat.label}</span>
            <strong>{stat.value}</strong>
            <small>{stat.detail}</small>
          </article>
        ))}
      </div>

      <div className="card-panel">
        <div className="panel-header">
          <h2>Legal activity</h2>
          <button type="button" className="ghost-button">View all</button>
        </div>
        <div className="activity-list">
          <div>
            <h3>Commercial dispute review</h3>
            <p>Drafting response to regulatory inquiry.</p>
          </div>
          <div>
            <h3>Employment advisory</h3>
            <p>Policy update and employment contract review due in 2 days.</p>
          </div>
          <div>
            <h3>Family trust planning</h3>
            <p>Documents uploaded for partner review.</p>
          </div>
        </div>
      </div>

      <div className="card-panel">
        <div className="panel-header">
          <h2>Recent updates</h2>
          <button type="button" className="ghost-button">Read</button>
        </div>
        <ul className="mini-list">
          {newsItems.slice(0, 4).map((item) => (
            <li key={item.id}>
              <span className="tag">{item.category}</span>
              <div>
                <strong>{item.title}</strong>
                <small>{item.date}</small>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}

function NewsEventsPage() {
  const [activeFilter, setActiveFilter] = useState<'All' | 'News' | 'Event'>('All')
  const filteredItems = activeFilter === 'All' ? newsItems : newsItems.filter((item) => item.category === activeFilter)

  return (
    <section className="news-page">
      <div className="news-toolbar">
        <div className="toolbar-tags">
          {(['All', 'News', 'Event'] as const).map((filter) => (
            <button key={filter} type="button" className={filter === activeFilter ? 'tag-button active' : 'tag-button'} onClick={() => setActiveFilter(filter)}>
              {filter}
            </button>
          ))}
        </div>
        <button type="button" className="ghost-button">Newest first</button>
      </div>

      <div className="news-list">
        {filteredItems.map((item) => (
          <article key={item.id} className="news-row">
            <img src={item.image} alt={item.title} />
            <div className="news-copy">
              <div className="news-header">
                <h3>{item.title}</h3>
                <div className="news-meta">
                  <span className="news-tag">{item.category}</span>
                  <div className="date-block">
                    <span>{item.date}</span>
                    <span>{item.time}</span>
                  </div>
                </div>
              </div>
              <p>{item.summary}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}

function BookingsPage() {
  return (
    <section className="simple-page">
      <div className="card-panel">
        <div className="panel-header">
          <h2>Bookings & Sessions</h2>
          <button type="button" className="primary-button small-button">Book a session</button>
        </div>
        <div className="timeline">
          <div className="timeline-item"><span className="timeline-dot" /><div><strong>Commercial advisory consultation</strong><p>Tuesday, 10:00 AM · Virtual</p></div></div>
          <div className="timeline-item"><span className="timeline-dot" /><div><strong>Employment law review</strong><p>Thursday, 2:30 PM · Lagos office</p></div></div>
          <div className="timeline-item"><span className="timeline-dot" /><div><strong>Contract compliance check</strong><p>Friday, 9:15 AM · Remote</p></div></div>
        </div>
      </div>
    </section>
  )
}

function RecentBookingsPage() {
  return (
    <section className="simple-page">
      <div className="card-panel">
        <div className="panel-header"><h2>Recent bookings</h2></div>
        <table className="data-table">
          <thead><tr><th>Session</th><th>Date</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>Corporate advisory</td><td>May 15, 2025</td><td><span className="status-badge success">Completed</span></td></tr>
            <tr><td>Employment review</td><td>May 07, 2025</td><td><span className="status-badge neutral">Reviewed</span></td></tr>
            <tr><td>Contract due diligence</td><td>Apr 29, 2025</td><td><span className="status-badge success">Completed</span></td></tr>
          </tbody>
        </table>
      </div>
    </section>
  )
}

function ProfilePage() {
  return (
    <section className="simple-page">
      <div className="card-panel profile-card">
        <div className="panel-header"><h2>Profile settings</h2><button type="button" className="ghost-button">Edit</button></div>
        <div className="profile-layout">
          <div className="profile-avatar-wrap"><img src="/images/portrait-03.jpg" alt="User profile" className="profile-avatar" /></div>
          <div className="profile-form-grid">
            <label>Full name<input type="text" defaultValue="Daniel Johnson" /></label>
            <label>Email<input type="email" defaultValue="daniel@hergers.com" /></label>
            <label>Phone<input type="tel" defaultValue="+234 809 000 8831" /></label>
            <label>Company<input type="text" defaultValue="Greenfield Capital" /></label>
          </div>
        </div>
      </div>
    </section>
  )
}

function PaymentsPage() {
  return (
    <section className="simple-page">
      <div className="card-panel">
        <div className="panel-header"><h2>Payment checkout</h2></div>
        <div className="invoice-box">
          <div className="invoice-row"><span>Legal consultation</span><strong>₦245,000</strong></div>
          <div className="invoice-row"><span>Document review</span><strong>₦120,000</strong></div>
          <div className="invoice-row total"><span>Total</span><strong>₦365,000</strong></div>
          <button type="button" className="primary-button">Proceed to payment</button>
        </div>
      </div>
    </section>
  )
}

function SupportPage() {
  return (
    <section className="simple-page">
      <div className="card-panel">
        <div className="panel-header"><h2>IT support</h2><button type="button" className="ghost-button">New ticket</button></div>
        <div className="support-list">
          <div className="support-item"><strong>Access issue to secure portal</strong><p>Status: In progress · Response within 4 hours</p></div>
          <div className="support-item"><strong>Client document upload failed</strong><p>Status: Resolved · Ticket closed</p></div>
        </div>
      </div>
    </section>
  )
}

function DocumentsPage() {
  return (
    <section className="simple-page">
      <div className="card-panel">
        <div className="panel-header"><h2>Documents</h2><button type="button" className="ghost-button">Upload</button></div>
        <ul className="file-list">
          <li>Board resolution.pdf</li>
          <li>Employment policy draft.docx</li>
          <li>Independent legal opinion.pdf</li>
          <li>Data privacy acknowledgement.pdf</li>
        </ul>
      </div>
    </section>
  )
}

function AuthShell({ badge, leftTitle, subTitle, formTitle, description, form }: { badge: string; leftTitle: string; subTitle: string; formTitle: string; description: string; form: ReactNode }) {
  return (
    <div className="auth-page-shell">
      <header className="auth-header">
        <div className="logo-inline">
          <img src={logoUrl} alt="Herger's & Co. logo" className="brand-mark" />
          <div className="logo-text">
            <span className="logo-name">{leftTitle}</span>
            <span className="logo-subtitle">{subTitle}</span>
          </div>
        </div>
        <div className="trust-badge">Trusted Legal Guidance<br />for a Stronger Tomorrow</div>
      </header>

      <main className="auth-layout">
        <section className="auth-hero-panel">
          <div className="hero-visual">
            <div className="hero-copy">
              <p className="eyebrow">{badge}</p>
              <h1>{leftTitle}</h1>
              <p className="helper-copy">Access your dashboard, book sessions, read the latest legal news and more.</p>
            </div>

            <div className="feature-stack">
              {featureList.map((item) => (
                <div key={item.title} className="feature-item">
                  <div className="feature-icon">{item.icon}</div>
                  <div>
                    <h3>{item.title}</h3>
                    <p>{item.text}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="hero-footer">
            <span>Don’t have an account?</span>
            <button type="button" className="primary-button small-button" onClick={() => window.location.assign('/signup')}>Sign Up <span>→</span></button>
          </div>
        </section>

        <section className="auth-form-panel">
          <div className="auth-copy">
            <p className="eyebrow secondary">{badge}</p>
            <h2>{formTitle}</h2>
            <p>{description}</p>
          </div>
          {form}
        </section>
      </main>
    </div>
  )
}

export default App
