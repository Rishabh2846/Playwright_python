import { test, expect } from '@playwright/test';

test('Hover', async ({ page }) => {

await page.goto('https://practice.expandtesting.com/hovers');
await page.getByTestId('img-user-1').hover();
await expect(page.getByRole('heading', { name: 'name: user1' })).toBeVisible();
await expect(page.getByRole('link', { name: 'View profile' })).toBeVisible();
await page.getByTestId('img-user-2').hover();
await expect(page.getByRole('heading', { name: 'name: user2' })).toBeVisible();
await expect(page.getByRole('link', { name: 'View profile' })).toBeVisible();
await page.getByTestId('img-user-3').hover();
await expect(page.getByRole('heading', { name: 'name: user3' })).toBeVisible();
await expect(page.getByRole('link', { name: 'View profile' })).toBeVisible();
await page.getByTestId('img-user-1').hover();
await page.getByRole('link', { name: 'View profile' }).click();
await expect(page.getByRole('heading', { name: 'Welcome user1' })).toBeVisible();
await page.getByRole('link', { name: 'Home' }).click();

 
});