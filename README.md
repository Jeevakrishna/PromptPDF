# PromptPDF

A modern web application that leverages AI to process and interact with PDF documents. Built with Next.js, TypeScript, and cutting-edge AI/ML technologies.

---

## Core Features

- **PDF Processing**: Upload and process PDF documents  
- **AI-Powered Chat**: Interactive chat interface for document-based Q&A  
- **Authentication**: Secure user authentication system  
- **File Management**: Organize and manage uploaded PDFs  
- **Responsive Design**: Works across desktop and mobile devices  

---

## Technology Stack

### Frontend
- **Next.js 15** – React framework for modern web apps  
- **TypeScript** – Strongly-typed JavaScript for scalability  
- **Tailwind CSS** – Utility-first styling framework  
- **shadcn/ui** – Accessible and customizable UI components  
- **TanStack Query** – State and data-fetching management  
- **Framer Motion** – Smooth, modern animations  

### Backend
- **Next.js API Routes** – Serverless API endpoints  
- **Drizzle ORM** – Type-safe database client  
- **PostgreSQL (Neon)** – Scalable cloud database  
- **AWS S3** – File storage for PDF uploads  

### AI/ML
- **LangChain** – Framework for building LLM-driven apps  
- **Google Generative AI** – Model integration for contextual chat  
- **Pinecone** – Vector database for semantic document search  

---

## Agile Development Overview

PromptPDF was developed following **Agile methodology** to ensure adaptability, collaboration, and rapid iteration between May 30 and July 14.

### Development Summary

| Role | Developer | Duration | Methodology | Key Focus Areas |
|------|------------|-----------|--------------|------------------|
| **Lead Developer** | **Jeevakrishna Vetrivel** | **May 30 – July 14, 2025** | **Agile (Scrum + Kanban Hybrid)** | PDF ingestion, RAG integration, UI/UX design, AI pipeline optimization |

### Agile Workflow Highlights

- **Sprint Planning:** Organized work into 3 major sprints (Core App, AI System, UI Polish)  
- **Daily Standups (Async):** Used GitHub Issues & Projects for task updates  
- **CI/CD Integration:** Automated builds and testing through GitHub Actions  
- **Iterative Testing:** Continuous feedback loop for performance and UX refinement  
- **Documentation:** Maintained changelogs, retrospectives, and sprint notes  

---

## RAG (Retrieval-Augmented Generation) Architecture

PromptPDF integrates a **RAG system** to enhance the accuracy and contextuality of AI-generated responses.

**Workflow:**
1. **Document Ingestion** → PDFs parsed and chunked into semantic units  
2. **Vectorization** → Chunks embedded using Google Generative AI embeddings  
3. **Vector Storage** → Stored in **Pinecone** for efficient semantic search  
4. **Context Retrieval** → Relevant chunks retrieved for each user query  
5. **Response Generation** → **LangChain** sends context to LLM for accurate answers  

---

## Getting Started

### Prerequisites
- Node.js 18+  
- PostgreSQL Database  
- AWS S3 Bucket  
- Google AI API Key  
- Pinecone API Key  

### Installation
1. **Clone the repository**
```bash
git clone https://github.com/your-username/PromptPDF.git
cd PromptPDF
```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

3. **Set up environment variables**
   Create a `.env.local` file in the root directory with the following variables:
   ```env
   DATABASE_URL=your_postgres_connection_string
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_REGION=your_aws_region
   AWS_BUCKET_NAME=your_s3_bucket_name
   GOOGLE_AI_API_KEY=your_google_ai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   NEXTAUTH_SECRET=your_nextauth_secret
   NEXTAUTH_URL=http://localhost:3000
   ```

4. **Run database migrations**
   ```bash
   npx drizzle-kit push:pg
   ```

5. **Start the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   ```

6. **Open [http://localhost:3000](http://localhost:3000) in your browser**

## Project Structure

```
src/
├── app/                    # App router pages and layouts
│   ├── api/               # API routes
│   │   ├── chat/          # Chat API endpoints
│   │   └── create-chat/   # Chat creation endpoints
│   └── chat/              # Chat interface
│       └── [chatId]/      # Individual chat sessions
├── components/            # Reusable UI components
├── lib/                   # Utility functions and configurations
└── drizzle/               # Database schema and migrations
```

## Development Workflow

1. **Branching Strategy**
   - `main` - Production-ready code
   - `develop` - Development integration branch
   - `feature/*` - New features
   - `bugfix/*` - Bug fixes

2. **Code Style**
   - Follow the [Next.js style guide](https://nextjs.org/docs/app/building-your-application/configuring/eslint)
   - Use TypeScript for type safety
   - Follow the existing code style and patterns

3. **Commits**
   - Write clear, descriptive commit messages
   - Reference issues when applicable

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Next.js](https://nextjs.org/) - The React Framework for Production
- [LangChain](https://www.langchain.com/) - Building applications with LLMs
- [shadcn/ui](https://ui.shadcn.com/) - Beautifully designed components
- [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework

## Author

**Jeevakrishna Vetrivel**
- LinkedIn: [Jeevakrishna Vetrivel](https://linkedin.com/in/jeevakrishna73)
- Portfolio: [Jeevakrishna Vetrivel](https://jeevakrishna-portfolio.vercel.app/)

