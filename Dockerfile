# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app
RUN useradd -m -u 1000 appuser
USER appuser
ENV HOME=/home/appuser
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Create a non-root user
RUN useradd -m -u 1000 appuser

# Switch to non-root user
USER appuser

# Copy installed packages from builder
COPY --from=builder /home/appuser/.local /home/appuser/.local

# Copy application code
COPY . .

# Change ownership of /app and /home/appuser/.local to appuser
#RUN chown -R appuser:appuser /app /home/appuser/.local

# Set PATH to include user's local bin
ENV PATH=/home/appuser/.local/bin:$PATH

# Expose port
EXPOSE 8080

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]