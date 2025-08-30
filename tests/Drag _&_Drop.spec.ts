import { test, expect } from '@playwright/test';

test('Drag and Drop', async ({ page }) => {
  await page.goto('https://practice.expandtesting.com/drag-and-drop');
  await expect(page.getByRole('heading', { name: 'Drag and Drop page for' })).toBeVisible();
  await expect(page.locator('#column-a')).toBeVisible();
 await expect(page.locator('#column-b')).toBeVisible();
 await page.locator('#column-a').dragTo(page.locator('#column-b'))
 await expect(page.locator('#column-a')).toBeVisible();
 await expect(page.locator('#column-b')).toBeVisible();

});