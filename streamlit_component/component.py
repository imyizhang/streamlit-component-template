# -*- coding: utf-8 -*-
"""Template component for Streamlit"""

from typing import Any, Optional

import streamlit as st


def component(container: Optional[Any] = None) -> None:
    """Add components to Streamlit app.

    Args:
        container (any, optional): Streamlit container. Defaults to `None`.
    """
    if container is None:
        container = st
