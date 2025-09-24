from flask import current_app
from config import db
from app import app

def run_migrations_online():
    """Run migrations in 'online' mode."""
    with app.app_context():
        # Configure the database connection
        with db.engine.connect() as connection:
            # Run the migration
            from alembic import context
            context.configure(
                connection=connection,
                target_metadata=db.metadata,
                compare_type=True,
                compare_server_default=True,
            )

            with context.begin_transaction():
                context.run_migrations()

if __name__ == '__main__':
    run_migrations_online()
