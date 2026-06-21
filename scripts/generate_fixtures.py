#!/usr/bin/env python
"""Script to generate test data fixtures."""

import json
from pathlib import Path
from datetime import datetime


def generate_stack_fixture():
    """Generate stack test fixture."""
    return {
        'operations': [
            {'op': 'push', 'value': 1, 'expected': 'success'},
            {'op': 'push', 'value': 2, 'expected': 'success'},
            {'op': 'push', 'value': 3, 'expected': 'success'},
            {'op': 'pop', 'expected': 3},
            {'op': 'peek', 'expected': 2},
        ]
    }


def generate_queue_fixture():
    """Generate queue test fixture."""
    return {
        'operations': [
            {'op': 'enqueue', 'value': 'a', 'expected': 'success'},
            {'op': 'enqueue', 'value': 'b', 'expected': 'success'},
            {'op': 'enqueue', 'value': 'c', 'expected': 'success'},
            {'op': 'dequeue', 'expected': 'a'},
            {'op': 'front', 'expected': 'b'},
        ]
    }


def generate_bst_fixture():
    """Generate BST test fixture."""
    return {
        'operations': [
            {'op': 'insert', 'value': 50, 'expected': True},
            {'op': 'insert', 'value': 30, 'expected': True},
            {'op': 'insert', 'value': 70, 'expected': True},
            {'op': 'insert', 'value': 20, 'expected': True},
            {'op': 'insert', 'value': 40, 'expected': True},
            {'op': 'search', 'value': 30, 'expected': True},
            {'op': 'search', 'value': 100, 'expected': False},
            {'op': 'inorder', 'expected': [20, 30, 40, 50, 70]},
        ]
    }


def generate_operation_log():
    """Generate sample operation log."""
    return {
        'timestamp': datetime.now().isoformat(),
        'operations': [
            {'timestamp': '2024-01-01T10:00:00', 'operation': 'push', 'value': 5, 'result': 'success'},
            {'timestamp': '2024-01-01T10:00:01', 'operation': 'push', 'value': 10, 'result': 'success'},
            {'timestamp': '2024-01-01T10:00:02', 'operation': 'pop', 'result': 'success'},
        ]
    }


def main():
    """Generate all fixtures."""
    fixtures_dir = Path(__file__).parent.parent / 'tests' / 'fixtures'
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate fixtures
    fixtures = {
        'stack_test.json': generate_stack_fixture(),
        'queue_test.json': generate_queue_fixture(),
        'bst_test.json': generate_bst_fixture(),
        'operation_log.json': generate_operation_log(),
    }
    
    # Save fixtures
    for filename, data in fixtures.items():
        filepath = fixtures_dir / filename
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Generated {filepath}")
    
    print("\nAll test fixtures generated successfully!")


if __name__ == '__main__':
    main()
